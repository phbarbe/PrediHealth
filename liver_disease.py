import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import RandomOverSampler

# Chargement des données
url = 'https://raw.githubusercontent.com/phbarbe/PrediHealth/main/liver_disease.csv'
liver_disease = pd.read_csv(url)

# Colonnes à supprimer
columns_to_drop = ['Dataset']

# Vérifier si les colonnes existent avant de les supprimer
columns_to_drop = [col for col in columns_to_drop if col in liver_disease.columns]

# Liste des colonnes à conserver
columns_list = [col for col in liver_disease.columns if col not in columns_to_drop]

def show():
    st.title("Liver Disease Prediction")
    st.header("Enter the following data:")

    # Assurez-vous que le DataFrame est chargé
    df = liver_disease

    # Préparation des données
    X = df[['Age', 'Gender', 'Total_Bilirubin', 'Direct_Bilirubin', 'Alkaline_Phosphotase', 'Alamine_Aminotransferase', 'Aspartate_Aminotransferase', 'Total_Protiens', 'Albumin', 'Albumin_and_Globulin_Ratio']]
    y = df['Dataset']

    # Convertir 'Gender' en variables numériques
    X['Gender'] = X['Gender'].map({'Male': 1, 'Female': 0})

    # Initialiser le RandomOverSampler
    ros = RandomOverSampler(random_state=42)

    # Resampler le dataset
    X_res, y_res = ros.fit_resample(X, y)

    # Diviser le dataset en ensembles d'entraînement et de test
    X_train_res, X_test_res, y_train_res, y_test_res = train_test_split(X_res, y_res, test_size=0.3, random_state=42)

    # Entraîner le modèle RandomForest
    rf_model = RandomForestClassifier(random_state=42)
    rf_model.fit(X_train_res, y_train_res)

    # Champs d'entrée pour les valeurs moyennes
    st.subheader("Entrer les données du patient")

    # Initialiser un dictionnaire pour stocker les entrées utilisateur
    user_input = {}
    
    for column in columns_list:
        label = column.replace("_", " ").title()
        if column == 'Gender':
            user_input[column] = st.selectbox(label, [0, 1], format_func=lambda x: 'Male' if x == 1 else 'Female', key=column)
        else:
            user_input[column] = st.number_input(label, format="%.2f", key=column)

    # Ajouter un bouton de soumission
    if st.button("Submit"):
        # Préparer les données d'entrée pour la prédiction
        input_data = [user_input[col] for col in X.columns]
        input_data_df = pd.DataFrame([input_data], columns=X.columns)
        prediction = rf_model.predict(input_data_df)
        st.write(f"Prediction: {'A risque' if prediction[0] == 1 else 'Pas à risque'}")

if __name__ == "__main__":
    show()
