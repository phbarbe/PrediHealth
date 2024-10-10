import pandas as pd
import streamlit as st
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt


# Chargement des données
url = 'https://raw.githubusercontent.com/MaskiVal/DataSets/main/cancer_breast.csv'
url = 'https://raw.githubusercontent.com/MaskiVal/DataSets/main/cancer_breast.csv'
breast_cancer = pd.read_csv(url)


# Colonnes à supprimer
columns_to_drop = ['id', 'Unnamed: 32', 'diagnosis']

# Vérifier si les colonnes existent avant de les supprimer
columns_to_drop = [col for col in columns_to_drop if col in breast_cancer.columns]

# Liste des colonnes à conserver
columns_list = [col for col in breast_cancer.columns if col not in columns_to_drop]

# Liste des colonnes avec p_value < 0.05
kruskal_result_list = [
    'perimeter_worst', 'radius_worst', 'area_worst', 
    'concave points_worst', 'concave points_mean', 'perimeter_mean', 'area_mean', 
    'concavity_mean', 'radius_mean', 'area_se', 'concavity_worst', 'perimeter_se', 
    'radius_se', 'compactness_mean', 'compactness_worst', 'texture_worst', 
    'concave points_se', 'texture_mean', 'concavity_se', 'smoothness_worst', 
    'symmetry_worst', 'smoothness_mean', 'compactness_se', 'symmetry_mean', 
    'fractal_dimension_worst', 'fractal_dimension_se', 'symmetry_se', 'smoothness_se', 
    'texture_se', 'fractal_dimension_mean'
]
main_kruskal_result_list = kruskal_result_list[0:27]

# Conversion de la colonne 'diagnosis' en float pour y
breast_cancer['diagnosis_float'] = breast_cancer['diagnosis'].apply(lambda x: 1 if x == 'M' else 0)

# X = colonnes de cancer_breast étant dans kruskal_result_list
X = breast_cancer[main_kruskal_result_list].select_dtypes('number')
y = breast_cancer['diagnosis_float']

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=42, stratify=y)

# Changement du poids des classes
# class 0 ('Benin')
class_weights = {0: 1, 1: 6}

# Création et entraînement du modèle
modelLR = LogisticRegression(random_state=42, class_weight=class_weights)
modelLR.fit(X_train, y_train)

# Liste des colonnes avec p_value < 0.05
kruskal_result_list = [
    'perimeter_worst', 'radius_worst', 'area_worst', 
    'concave points_worst', 'concave points_mean', 'perimeter_mean', 'area_mean', 
    'concavity_mean', 'radius_mean', 'area_se', 'concavity_worst', 'perimeter_se', 
    'radius_se', 'compactness_mean', 'compactness_worst', 'texture_worst', 
    'concave points_se', 'texture_mean', 'concavity_se', 'smoothness_worst', 
    'symmetry_worst', 'smoothness_mean', 'compactness_se', 'symmetry_mean', 
    'fractal_dimension_worst', 'fractal_dimension_se', 'symmetry_se', 'smoothness_se', 
    'texture_se', 'fractal_dimension_mean'
]
main_kruskal_result_list = kruskal_result_list[0:27]

# Conversion de la colonne 'diagnosis' en float pour y
breast_cancer['diagnosis_float'] = breast_cancer['diagnosis'].apply(lambda x: 1 if x == 'M' else 0)

# X = colonnes de cancer_breast étant dans kruskal_result_list
X = breast_cancer[main_kruskal_result_list].select_dtypes('number')
y = breast_cancer['diagnosis_float']

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=42, stratify=y)

# Changement du poids des classes
# class 0 ('Benin')
class_weights = {0: 1, 1: 6}

# Création et entraînement du modèle
modelLR = LogisticRegression(random_state=42, class_weight=class_weights)
modelLR.fit(X_train, y_train)

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
    return st.number_input(label, min_value=min_value, value=value, format=format, key=column)
    return st.number_input(label, min_value=min_value, value=value, format=format, key=column)

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

# Colonnes pour les 8 valeurs principales
top_8_columns = ['perimeter_worst', 'radius_worst', 'area_worst', 'concave points_worst', 'concave points_mean', 'perimeter_mean', 'area_mean', 'concavity_mean']

# Colonnes pour les autres valeurs
other_columns = ['radius_mean', 'area_se', 'concavity_worst', 'perimeter_se', 'radius_se', 'compactness_mean', 'compactness_worst', 'texture_worst', 'concave points_se', 'texture_mean', 'concavity_se', 'smoothness_worst', 'symmetry_worst', 'smoothness_mean', 'compactness_se', 'symmetry_mean', 'fractal_dimension_worst', 'fractal_dimension_se', 'symmetry_se']


def show():
    st.title("Breast Cancer Prediction")

    # Centrer les éléments en utilisant des colonnes
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.header("Enter the following data:")

        # Assurez-vous que le DataFrame est chargé
        df = breast_cancer

        # Dictionnaire pour stocker les valeurs saisies
        user_inputs = {}

        # Input fields for the top 8 values
        st.subheader("Top 8 Values")
        for column in top_8_columns:
            label = column.replace("_", " ").title()
            user_inputs[column] = create_number_input(label, df, column)
            display_statistics(df, column, label)

        # Input fields for the other values
        st.subheader("Other Values")
        for column in other_columns:
            label = column.replace("_", " ").title()
            user_inputs[column] = create_number_input(label, df, column)
            display_statistics(df, column, label)

    # Utiliser un conteneur pour afficher le pairplot sur toute la largeur
    container = st.container()

    with container:
        # Add a submit button
        if st.button("Submit"):
            st.write("Data submitted successfully!")
            # Convertir les entrées utilisateur en DataFrame pour la prédiction
            input_data = pd.DataFrame([user_inputs])
            prediction = modelLR.predict(input_data)[0]
            prediction_proba = modelLR.predict_proba(input_data)[0]

            # Afficher le résultat de la prédiction
            result = 'Malignant' if prediction == 1 else 'Benign'
            st.write(f"The model predicts: **{result}** with a probability of {100*prediction_proba[prediction]:.2f}%.")
            st.write(f"Disclaimer: This prediction is informative and does not replace a professional medical diagnosis.")

            # Afficher le pairplot avec les données du patient examiné
            # Créer un DataFrame 'cancer_breast_TOP8' ne conservant que les colonnes spécifiques
            cancer_breast_TOP8 = breast_cancer[['diagnosis', 'perimeter_worst', 'radius_worst', 'area_worst', 'concave points_worst', 'concave points_mean', 'perimeter_mean', 'area_mean', 'concavity_mean']]
            
            # Créer le pairplot
            pairplot = sns.pairplot(cancer_breast_TOP8, hue='diagnosis', palette={'B': '#10989c', 'M': '#ef6763'}, plot_kws={'alpha':0.5}, corner=True)

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
                    ax.scatter(input_data[x_var].values, input_data[y_var].values, color='yellow', s=100, edgecolor='#34495E', alpha=0.8)
            
            # Ajuster la taille de la figure pour qu'elle utilise toute la largeur
            pairplot.fig.set_size_inches(18, 18)

            # Afficher le graphique dans Streamlit
            st.pyplot(pairplot)

if __name__ == "__main__":
    show()


