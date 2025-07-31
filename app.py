from flask import Flask, request, jsonify
import pandas as pd
import xgboost as xgb
import joblib
import json
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# Load the model and necessary files
model = xgb.Booster()
model.load_model('./model/advanced_json_model.json')
scaler = joblib.load('./model/minmax_scaler.pkl')
# train_columns = pd.read_csv('./model/preprocessed_data.csv').drop('remuneracion', axis=1).columns
preprocessor = joblib.load('./model/preprocessor.pkl')

# Para Alinear columnas con el modelo
with open('./model/train_columns.json', 'r', encoding='utf-8') as f:
    train_columns = json.load(f)

# raw_data_path = './dataset/2020.csv'  # Ruta del archivo de datos sin procesar
# raw_data = pd.read_csv(raw_data_path, delimiter=';')

with open('./model/form_options.json', 'r', encoding='utf-8') as f:
    options_per_column = json.load(f)


# Define categorical columns
categorical_columns = [
    'rango_edad', 'regimen_laboral', 'nivel_educativo', 'regimen_salud',
    'tamaão_empresa', 'sexo', 'departamento', 'actividad_economica',
    'regimen_pension', 'ocupacion'
]

# Preprocessing pipeline
# categorical_imputer = SimpleImputer(strategy='most_frequent')
# preprocessor = ColumnTransformer(
#     transformers=[
#         ('cat', Pipeline([
#             ('imputer', categorical_imputer),
#             ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
#         ]), categorical_columns)
#     ]
# )

@app.route("/predict", methods=["POST"])
def predict():
    try:
        user_input = request.json  # Input as JSON
        input_df = pd.DataFrame([user_input])

        # Preprocess input
        def handle_no_determinado(column):
            if column.dtype == 'object' or column.dtype.name == 'category':
                return column.fillna('NO DETERMINADO').replace('NO DETERMINADO', 'NoDeterminado')
            return column.fillna(column.median())

        for col in input_df.columns:
            input_df[col] = handle_no_determinado(input_df[col])

        # preprocessed_input = preprocessor.fit_transform(input_df)
        preprocessed_input = preprocessor.transform(input_df)
        ohe_columns = preprocessor.transformers_[0][1].named_steps['onehot'].get_feature_names_out(categorical_columns)
        aligned_df = pd.DataFrame(preprocessed_input, columns=ohe_columns)

        # Identificar columnas faltantes y concatenar
        missing_columns = [col for col in train_columns if col not in aligned_df.columns]
        missing_df = pd.DataFrame(0, index=aligned_df.index, columns=missing_columns)
        aligned_df = pd.concat([aligned_df, missing_df], axis=1)
        aligned_df = aligned_df[train_columns]  # Ordenar las columnas

        dmatrix = xgb.DMatrix(aligned_df)
        predictions = model.predict(dmatrix)
        predictions_original_scale = scaler.inverse_transform(predictions.reshape(-1, 1))

        return jsonify({"prediction": float(predictions_original_scale.flatten()[0])})
    except Exception as e:
        return jsonify({"error": str(e)})


@app.route('/get-options', methods=['GET'])
def get_options():

    return jsonify(options_per_column)


if __name__ == "__main__":
    app.run(debug=True)

