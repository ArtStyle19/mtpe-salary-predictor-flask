# 📊 Predicción de Sueldos MTPE - Perú

## 👨‍💻 Developed by Jorge Guillermo Olarte Quispe

## 🏫 Universidad Nacional del Altiplano – Ingeniería de Sistemas

**Predicción automatizada de remuneraciones mensuales en el sector privado peruano**  
Aplicación web basada en inteligencia artificial que estima el sueldo mensual de un trabajador en función de características demográficas y laborales. Utiliza datos abiertos del **Ministerio de Trabajo y Promoción del Empleo (MTPE)** y un modelo de machine learning (XGBoost) entrenado con datos reales.

---

## 🗂️ Estructura del Proyecto

| Módulo              | Descripción                                          | Repositorio                                                                                    |
| ------------------- | ---------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| 🖥️ Frontend         | Interfaz web en React + Tailwind para ingresar datos | [`mtpe-salary-predictor-react`](https://github.com/ArtStyle19/mtpe-salary-predictor-react)     |
| 🔁 Backend          | API REST en Flask con modelo XGBoost                 | [`backend-mtpe-salary-predictor`](https://github.com/ArtStyle19/backend-mtpe-salary-predictor) |
| 🧹 Preprocesamiento | Limpieza, codificación y entrenamiento del modelo    | Privado                                                                                        |

---

## 🎯 Objetivo del Proyecto

Diseñar un sistema que, a partir de atributos como **edad, nivel educativo, ocupación, ubicación, tamaño de empresa, entre otros**, pueda predecir el sueldo mensual de un trabajador formal privado en Perú.

---

## ⚙️ Tecnologías Utilizadas

- **Frontend:** React, TypeScript, TailwindCSS, Fetch API
- **Backend:** Python, Flask, XGBoost, Scikit-learn, Pandas, Joblib
- **Preprocesamiento:** OneHotEncoder, MinMaxScaler, Pipelines automáticos
- **Dataset:** MTPE Perú (2020-2023, datos semestrales)

---

## 🧠 Proceso de Modelado Predictivo

1. 📥 **Carga de datos:** CSV delimitado por `;` con +10 columnas relevantes.
2. 🧹 **Preprocesamiento:**
   - Imputación de valores "NO DETERMINADO"
   - Codificación One-Hot para variables categóricas
   - Normalización con MinMaxScaler
3. 🔄 **Automatización:** Pipeline con `ColumnTransformer` + persistencia con `joblib`
4. 📈 **Modelado:** Entrenamiento con XGBoost (regresión) y validación con MAE y RMSE
5. 🧪 **Evaluación:** El error promedio entre la predicción y el valor real fue de aproximadamente 844.85 soles peruanos (PEN).
6. 💾 **Despliegue:** Backend con API `/predict` y `/get-options` + frontend dinámico

---

## 📈 Evaluación del Modelo

### 🔍 Dispersión: Real vs Predicho

![real_vs_pred](images/real_vs_pred.png)

### 📉 Error Absoluto vs Sueldo Real

![abs_error_vs_real](images/abs_error_vs_real.png)

### 📊 Distribución del Error Absoluto

![hist_abs_error](images/hist_abs_error.png)

---

## 🧬 Importancia de Variables (XGBoost)

### 🎯 Feature Importance - Weight

![importance_weight](images/importance_weight.png)

### 🎯 Feature Importance - Gain

![importance_gain](images/importance_gain.png)

### 🎯 Feature Importance - Cover

![importance_cover](images/importance_cover.png)

---

## 👷‍♂️ Ejemplos de Perfiles Analizados (Visuales)

Estos perfiles visuales ayudan a contextualizar los escenarios laborales representados en el modelo:

| Imagen                                                           | Descripción                          |
| ---------------------------------------------------------------- | ------------------------------------ |
| ![varon_lima](images/varon_obrero_lima.jpg)                      | Varón obrero en Lima                 |
| ![mujer_salud](images/mujer_sector_salud.jpg)                    | Mujer trabajadora en salud           |
| ![mineria](images/varon_sector_mineria.jpg)                      | Varón en sector minería              |
| ![ind_manuf](images/varon_tecnico_sector_ind_manufactureras.jpg) | Técnico en industrias manufactureras |
| ![construccion](images/varon_obrero_construccion.jpg)            | Varón obrero en construcción         |

---

## 🧾 Licencia

Este proyecto es de uso académico y de investigación. Los datos pertenecen al MTPE y están bajo licencias de uso abierto.

---
