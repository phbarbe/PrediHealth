import pandas as pd
import streamlit as st

# Chargement des données
url = 'https://raw.githubusercontent.com/MaskiVal/DataSets/main/cancer_breast.csv'
breast_cancer = pd.read_csv(url)

# Colonnes à supprimer
columns_to_drop = ['id', 'Unnamed: 32', 'diagnosis']

# Vérifier si les colonnes existent avant de les supprimer
columns_to_drop = [col for col in columns_to_drop if col in breast_cancer.columns]

# Liste des colonnes à conserver
columns_list = [col for col in breast_cancer.columns if col not in columns_to_drop]

def get_quantile_value(df, column, quantile):
    """
    Cette fonction retourne la valeur du quantile spécifié pour une colonne donnée du DataFrame.
    """
    return df[df['diagnosis'] == 'B'].drop(columns_to_drop, axis=1).quantile(quantile)[column]

def create_number_input(label, df, column, quantile=0.5, min_value=0.0, format="%.4f"):
    """
    Crée un champ de saisie pour un nombre dans Streamlit avec une valeur par défaut basée sur le quantile spécifié.
    """
    value = get_quantile_value(df, column, quantile)
    return st.number_input(label, min_value=min_value, value=value, format=format)

def display_statistics(df, column, label):
    """
    Cette fonction affiche les statistiques (Q1, médiane, Q3) pour une colonne donnée.
    """
    Q1 = get_quantile_value(df, column, 0.25)
    median = get_quantile_value(df, column, 0.5)
    Q3 = get_quantile_value(df, column, 0.75)
    
    with st.expander(f"See benign quantiles for {label}"):
        st.write(f"{label} - 25% < {Q1:.4f}")
        st.write(f"{label} - 50% < {median:.4f}")
        st.write(f"{label} - 75% < {Q3:.4f}")

def show():
    st.title("Breast Cancer Prediction")
    st.header("Enter the following data:")

    # Assurez-vous que le DataFrame est chargé
    df = breast_cancer

    # Input fields for the mean values
    st.subheader("Mean Values")
    
    for column in columns_list:
        label = column.replace("_", " ").title()
        create_number_input(label, df, column)
        display_statistics(df, column, label)

    # Add a submit button
    if st.button("Submit"):
        st.write("Data submitted successfully!")
        # Add the code for prediction or further processing here

if __name__ == "__main__":
    show()
