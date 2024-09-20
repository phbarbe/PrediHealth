import streamlit as st
import pandas as pd
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.utils import resample

# Chargement des données
url = 'https://raw.githubusercontent.com/Ieric03/dataset/main/kidney_disease.csv'
df_origine = pd.read_csv(url)

# Suppression de la colonne 'id'
df_origine.drop("id", axis=1, inplace=True)

# Renommer les colonnes
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

# Traitement des valeurs manquantes
imputer = SimpleImputer(strategy='mean')
for column in df_origine.columns:
    if df_origine[column].dtype == 'object':
        df_origine[column].fillna(df_origine[column].mode()[0], inplace=True)
    else:
        df_origine[column] = imputer.fit_transform(df_origine[[column]])

# Encodage des colonnes catégoriques
label_encoders = {}
for column in df_origine.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    df_origine[column] = le.fit_transform(df_origine[column])
    label_encoders[column] = le

# Standardisation des colonnes numériques
scaler = StandardScaler()
scaled_columns = df_origine.columns[df_origine.dtypes != 'object']
df_origine[scaled_columns] = scaler.fit_transform(df_origine[scaled_columns])

# Ajustement de la colonne 'Classification'
df_origine['Classification'] = df_origine['Classification'].apply(lambda x: 1 if x > 0 else 0)

# Équilibrage des classes via le suréchantillonnage
df_majority = df_origine[df_origine.Classification == 0]
df_minority = df_origine[df_origine.Classification == 1]
df_minority_upsampled = resample(df_minority, replace=True, n_samples=len(df_majority), random_state=123)
df_upsampled = pd.concat([df_majority, df_minority_upsampled])

# Séparation des données
X = df_upsampled.drop('Classification', axis=1)
y = df_upsampled['Classification']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modèle RandomForest
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)

# Interface Streamlit
def show():
    st.title("Kidney Disease Prediction")

    # Centrer les éléments en utilisant des colonnes
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        st.header("Enter the following data:")

        # Entrées utilisateur
        user_input = {}
        for column in X.columns:
            label = column.replace("_", " ").title()
            user_input[column] = st.number_input(label, format="%.2f", key=column)

        # Soumission des données utilisateur
        if st.button("Submit"):
            input_data = [user_input[col] for col in X.columns]
            input_data_df = pd.DataFrame([input_data], columns=X.columns)
            prediction = rf_model.predict(input_data_df)
            st.write(f"Prediction: {'At risk' if prediction[0] == 1 else 'Not at risk'}")

            st.write(f"Disclaimer: This prediction is informative and does not replace a professional medical diagnosis.")

            # Affichage du graphique pairplot avec les données de l'utilisateur
            pairplot = sns.pairplot(df_origine, hue='Classification', palette={1: '#10989c', 0: '#ef6763'}, plot_kws={'alpha': 0.5}, corner=True)

            # Ajout des données utilisateur dans le graphique
            for i in range(pairplot.axes.shape[0]):
                for j in range(i):
                    ax = pairplot.axes[i, j]
                    x_var = pairplot.x_vars[j]
                    y_var = pairplot.y_vars[i]
                    ax.scatter(input_data_df[x_var].values, input_data_df[y_var].values, color='yellow', s=100, edgecolor='#34495E', alpha=0.8)

            pairplot.fig.set_size_inches(18, 18)
            st.pyplot(pairplot)

if __name__ == "__main__":
    show()
