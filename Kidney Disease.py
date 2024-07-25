import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.utils import resample
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split

# Charger le dataset
url = "https://raw.githubusercontent.com/Ieric03/dataset/main/kidney_disease.csv"
df_origine = pd.read_csv(url)

# Suppression de la colonne "id" pas utile
df_origine.drop("id", axis=1, inplace=True)

# Renommer les colonnes pour correspondre à celles utilisées précédemment
column_mapping = {
    "age": "Age", "bp": "Blood Pressure", "sg": "Specific Gravity",
    "al": "Albumin", "su": "Sugar", "rbc": "Red Blood Cells",
    "pc": "Pus Cell", "pcc": "Pus Cell Clumps", "ba": "Bacteria",
    "bgr": "Blood Glucose Random", "bu": "Blood Urea", "sc": "Serum Creatinine",
    "sod": "Sodium", "pot": "Potassium", "hemo": "Hemoglobin",
    "pcv": "Packed Cell Volume", "wc": "White Blood Cell Count", "rc": "Red Blood Cell Count",
    "htn": "Hypertension", "dm": "Diabetes Mellitus", "cad": "Coronary Artery Disease",
    "appet": "Appetite", "pe": "Pedal Edema", "ane": "Anemia", "classification": "Classification"
}
df_origine.rename(columns=column_mapping, inplace=True)

# Nettoyage des valeurs 'ckd\t' dans la colonne 'classification'
df_origine['Classification'] = df_origine['Classification'].str.strip()

# Gestion des valeurs manquantes
imputer = SimpleImputer(strategy='mean')
for column in df_origine.columns:
    if df_origine[column].dtype == 'object':
        df_origine[column].fillna(df_origine[column].mode()[0], inplace=True)
    else:
        df_origine[column] = imputer.fit_transform(df_origine[[column]])

# Transformation des variables catégorielles
label_encoders = {}
for column in df_origine.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    df_origine[column] = le.fit_transform(df_origine[column])
    label_encoders[column] = le

# Normalisation des données
scaler = StandardScaler()
scaled_columns = df_origine.columns[df_origine.dtypes != 'object']
df_origine[scaled_columns] = scaler.fit_transform(df_origine[scaled_columns])

# Conversion de la colonne 'classification' en binaire
df_origine['Classification'] = df_origine['Classification'].apply(lambda x: 1 if x == 'ckd' else 0)

# Vérification des valeurs uniques dans la colonne 'Classification'
st.write("Valeurs uniques dans la colonne 'Classification' :", df_origine['Classification'].unique())

# Vérification des classes
if df_origine['Classification'].nunique() != 2:
    st.error("La colonne 'Classification' doit contenir exactement deux classes (0 et 1).")

# Gestion du déséquilibre des classes
df_majority = df_origine[df_origine.Classification == 0]
df_minority = df_origine[df_origine.Classification == 1]

# Vérifiez les tailles des classes
# st.write("Taille de la classe majoritaire :", df_majority.shape)
# st.write("Taille de la classe minoritaire :", df_minority.shape)

if df_majority.empty or df_minority.empty:
    st.error("Il doit y avoir au moins un exemple dans chaque classe.")

if not df_majority.empty and not df_minority.empty:
    df_minority_upsampled = resample(df_minority,
                                     replace=True,     # échantillonnage avec remplacement
                                     n_samples=len(df_majority),    # pour correspondre au nombre de la classe majoritaire
                                     random_state=123) # pour la reproductibilité

df_upsampled = pd.concat([df_majority, df_minority_upsampled])

    # Séparation des données en ensembles d'entraînement et de test
X = df_upsampled.drop('Classification', axis=1)
y = df_upsampled['Classification']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Entraînement du modèle RandomForest
model = RandomForestClassifier()
model.fit(X_train, y_train)

    # Préparation des valeurs moyennes pour préremplir les champs
mean_values = df_origine.mean()

st.title("Prédiction de Maladie Rénale Chronique")

    # Formulaire pour entrer les valeurs des variables
age = st.number_input("Age", value=float(mean_values["Age"]))
blood_pressure = st.number_input("Blood Pressure", value=float(mean_values["Blood Pressure"]))
specific_gravity = st.number_input("Specific Gravity", value=float(mean_values["Specific Gravity"]))
albumin = st.number_input("Albumin", value=float(mean_values["Albumin"]))
sugar = st.number_input("Sugar", value=float(mean_values["Sugar"]))
blood_glucose_random = st.number_input("Blood Glucose Random", value=float(mean_values["Blood Glucose Random"]))
blood_urea = st.number_input("Blood Urea", value=float(mean_values["Blood Urea"]))
serum_creatinine = st.number_input("Serum Creatinine", value=float(mean_values["Serum Creatinine"]))
sodium = st.number_input("Sodium", value=float(mean_values["Sodium"]))
potassium = st.number_input("Potassium", value=float(mean_values["Potassium"]))
hemoglobin = st.number_input("Hemoglobin", value=float(mean_values["Hemoglobin"]))
packed_cell_volume = st.number_input("Packed Cell Volume", value=float(mean_values["Packed Cell Volume"]))
white_blood_cell_count = st.number_input("White Blood Cell Count", value=float(mean_values["White Blood Cell Count"]))
red_blood_cell_count = st.number_input("Red Blood Cell Count", value=float(mean_values["Red Blood Cell Count"]))
hypertension = st.selectbox("Hypertension", ["yes", "no"], index=int(mean_values["Hypertension"]))
diabetes_mellitus = st.selectbox("Diabetes Mellitus", ["yes", "no"], index=int(mean_values["Diabetes Mellitus"]))
coronary_artery_disease = st.selectbox("Coronary Artery Disease", ["yes", "no"], index=int(mean_values["Coronary Artery Disease"]))
appetite = st.selectbox("Appetite", ["good", "poor"], index=int(mean_values["Appetite"]))
pedal_edema = st.selectbox("Pedal Edema", ["yes", "no"], index=int(mean_values["Pedal Edema"]))
anemia = st.selectbox("Anemia", ["yes", "no"], index=int(mean_values["Anemia"]))

    # Ajouter un bouton pour effectuer une prédiction
if st.button("Prédire"):
    input_data = pd.DataFrame({
        "Age": [age],
        "Blood Pressure": [blood_pressure],
        "Specific Gravity": [specific_gravity],
        "Albumin": [albumin],
        "Sugar": [sugar],
        "Blood Glucose Random": [blood_glucose_random],
        "Blood Urea": [blood_urea],
        "Serum Creatinine": [serum_creatinine],
        "Sodium": [sodium],
        "Potassium": [potassium],
        "Hemoglobin": [hemoglobin],
        "Packed Cell Volume": [packed_cell_volume],
        "White Blood Cell Count": [white_blood_cell_count],
        "Red Blood Cell Count": [red_blood_cell_count],
        "Hypertension": [1 if hypertension == "yes" else 0],
        "Diabetes Mellitus": [1 if diabetes_mellitus == "yes" else 0],
        "Coronary Artery Disease": [1 if coronary_artery_disease == "yes" else 0],
        "Appetite": [1 if appetite == "good" else 0],
        "Pedal Edema": [1 if pedal_edema == "yes" else 0],
        "Anemia": [1 if anemia == "yes" else 0]
    })

    st.write("Données d'entrée pour la prédiction :")
    st.write(input_data)

        # Utiliser le modèle RandomForest pour la prédiction   
    prediction = model.predict(input_data)
    prediction_proba = model.predict_proba(input_data)

    st.write("Prédiction :")
    st.write("Maladie Rénale Chronique" if prediction[0] == 1 else "Pas de Maladie Rénale Chronique")
    st.write("Probabilité :")
    st.write(prediction_proba)
