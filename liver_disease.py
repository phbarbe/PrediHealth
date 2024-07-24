import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import RandomOverSampler
import seaborn as sns

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
    st.subheader("Enter patient data:")

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
        st.write(f"Prediction: {'At risk' if prediction[0] == 1 else 'Not at risk'}")

        st.write(f"Disclaimer: This prediction is informative and does not replace a professional medical diagnosis.")

        # Créer le pairplot
        pairplot = sns.pairplot(liver_disease, hue='Dataset', palette={1: '#10989c', 2: '#ef6763'}, plot_kws={'alpha':0.5}, corner=True)

        # Modifier la couleur de fond de chaque axe
        for ax in pairplot.axes.flatten():
            if ax is not None:
                ax.set_facecolor('#E3E3E3')

        # Modifier la couleur de fond de la figure
        pairplot.fig.patch.set_facecolor('#E3E3E3')

        # Ajouter les données du patient examiné sur chaque graphique du pairplot
        for i in range(pairplot.axes.shape[0]):
            for j in range(i):  # Only iterate over the lower triangle
                ax = pairplot.axes[i, j]
                x_var = pairplot.x_vars[j]
                y_var = pairplot.y_vars[i]
                ax.scatter(input_data_df[x_var].values, input_data_df[y_var].values, color='yellow', s=100, edgecolor='#34495E', alpha=0.8)
        
        # Ajuster la taille de la figure pour qu'elle utilise toute la largeur
        pairplot.fig.set_size_inches(18, 18)

        # Afficher le graphique dans Streamlit
        st.pyplot(pairplot)

if __name__ == "__main__":
    show()
