import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt

# Chargement des données
df = pd.read_csv('https://raw.githubusercontent.com/phbarbe/PrediHealth/main/maladie_cardiaque.csv')  # Remplacez par le chemin vers vos données

# Sélection explicite des colonnes pour X et y
colonnes_X = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
X = df[colonnes_X]
y = df['target']

# Division des données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Initialiser le scaler
scaler = StandardScaler()


# Ajuster le scaler uniquement sur les données d'entraînement
X_train_scaled = scaler.fit_transform(X_train)

# Initialiser et entraîner le modèle
model = RandomForestClassifier(random_state=0)
model.fit(X_train_scaled, y_train)

# Standardiser les données de test
X_test_scaled = scaler.transform(X_test)

# Fonction pour faire des prédictions basées sur les entrées utilisateur
def predire_maladie(model, scaler, user_input, feature_names):
    """
    Prédit si un utilisateur a une maladie ou non en fonction de ses valeurs d'entrée.

    Args:
    - model: Modèle RandomForestClassifier entraîné.
    - scaler: StandardScaler utilisé pour les caractéristiques.
    - user_input: Liste ou tableau des caractéristiques d'entrée.
    - feature_names: Liste des noms des caractéristiques.

    Returns:
    - Prédiction: 1 si l'utilisateur est prédit avoir la maladie, 0 sinon.
    """
    # Convertir les entrées utilisateur en DataFrame
    user_input_df = pd.DataFrame([user_input], columns=feature_names)
    
    # Standardiser les entrées si nécessaire
    user_input_scaled = scaler.transform(user_input_df)
    
    # Faire la prédiction
    prediction = model.predict(user_input_scaled)
    
    return prediction[0]

# Liste des noms des caractéristiques
feature_names = colonnes_X

# Interface utilisateur Streamlit
def show():
    st.title('Prédiction de Maladie avec RandomForest')

    # Créer des entrées utilisateur
    user_inputs = {}
    for feature in feature_names:
        value = st.number_input(f'{feature}', value=0.0, step=0.01)
        user_inputs[feature] = value

    user_input_list = [user_inputs[feature] for feature in feature_names]

    # Faire la prédiction
    if st.button('Faire la prédiction'):
        resultat = predire_maladie(model, scaler, user_input_list, feature_names)
        st.write(f'La prédiction est : {"Maladie" if resultat == 1 else "Pas de Maladie"}')

        # Créer un pairplot avec les données
        pairplot = sns.pairplot(df, hue='target', palette={1: '#10989c', 0: '#ef6763'}, plot_kws={'alpha':0.5}, corner=True)
        
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
                ax.scatter(user_input_list[j], user_input_list[i], color='yellow', s=100, edgecolor='#34495E', alpha=0.8)

        # Ajuster la taille de la figure pour qu'elle utilise toute la largeur
        pairplot.fig.set_size_inches(18, 18)

        # Afficher le graphique dans Streamlit
        st.pyplot(pairplot)

if __name__ == "__main__":
    show()
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt

# Chargement des données
df = pd.read_csv('C:/Users/ahmed/OneDrive/Desktop/Mini_projet_festivale/maladie_cardiaque.csv')  # Remplacez par le chemin vers vos données

# Sélection explicite des colonnes pour X et y
colonnes_X = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
X = df[colonnes_X]
y = df['target']

# Division des données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Initialiser le scaler
scaler = StandardScaler()

# Ajuster le scaler uniquement sur les données d'entraînement
X_train_scaled = scaler.fit_transform(X_train)

# Initialiser et entraîner le modèle
model = RandomForestClassifier(random_state=0)
model.fit(X_train_scaled, y_train)

# Standardiser les données de test
X_test_scaled = scaler.transform(X_test)

# Fonction pour faire des prédictions basées sur les entrées utilisateur
def predire_maladie(model, scaler, user_input, feature_names):
    """
    Prédit si un utilisateur a une maladie ou non en fonction de ses valeurs d'entrée.

    Args:
    - model: Modèle RandomForestClassifier entraîné.
    - scaler: StandardScaler utilisé pour les caractéristiques.
    - user_input: Liste ou tableau des caractéristiques d'entrée.
    - feature_names: Liste des noms des caractéristiques.

    Returns:
    - Prédiction: 1 si l'utilisateur est prédit avoir la maladie, 0 sinon.
    """
    # Convertir les entrées utilisateur en DataFrame
    user_input_df = pd.DataFrame([user_input], columns=feature_names)
    
    # Standardiser les entrées si nécessaire
    user_input_scaled = scaler.transform(user_input_df)
    
    # Faire la prédiction
    prediction = model.predict(user_input_scaled)
    
    return prediction[0]

# Liste des noms des caractéristiques
feature_names = colonnes_X

# Interface utilisateur Streamlit
def show():
    st.title('Prédiction de Maladie avec RandomForest')

    # Créer des entrées utilisateur
    user_inputs = {}
    for feature in feature_names:
        value = st.number_input(f'{feature}', value=0.0, step=0.01)
        user_inputs[feature] = value

    user_input_list = [user_inputs[feature] for feature in feature_names]

    # Faire la prédiction
    if st.button('Faire la prédiction'):
        resultat = predire_maladie(model, scaler, user_input_list, feature_names)
        st.write(f'La prédiction est : {"Maladie" if resultat == 1 else "Pas de Maladie"}')

        # Créer un pairplot avec les données
        pairplot = sns.pairplot(df, hue='target', palette={1: '#10989c', 0: '#ef6763'}, plot_kws={'alpha':0.5}, corner=True)
        
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
                ax.scatter(user_input_list[j], user_input_list[i], color='yellow', s=100, edgecolor='#34495E', alpha=0.8)

        # Ajuster la taille de la figure pour qu'elle utilise toute la largeur
        pairplot.fig.set_size_inches(18, 18)

        # Afficher le graphique dans Streamlit
        st.pyplot(pairplot)

if __name__ == "__main__":
    show()

