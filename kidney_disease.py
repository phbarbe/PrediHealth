import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import warnings
warnings.filterwarnings("ignore")

url =pd.read_csv("https://raw.githubusercontent.com/Ieric03/dataset/main/kidney_disease.csv")
df_origine = pd.DataFrame(url)

df_origine.drop("id", axis=1,inplace=True)

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

valeur_manquante = df_origine.isnull().sum()
pourcentage_manquant = (valeur_manquante / len(df_origine)) * 100

class_counts = df_origine['Classification'].value_counts()
df_origine['Classification'] = df_origine['Classification'].replace('ckd\t', 'ckd')

from sklearn.impute import SimpleImputer
from sklearn.utils import resample
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier

imputer = SimpleImputer(strategy='mean')
for column in df_origine.columns:
    if df_origine[column].dtype == 'object':
        df_origine[column].fillna(df_origine[column].mode()[0], inplace=True)
    else:
        df_origine[column] = imputer.fit_transform(df_origine[[column]])
label_encoders = {}
for column in df_origine.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    df_origine[column] = le.fit_transform(df_origine[column])
    label_encoders[column] = le
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaled_columns = df_origine.columns[df_origine.dtypes != 'object']
df_origine[scaled_columns] = scaler.fit_transform(df_origine[scaled_columns])

df_origine['Classification'] = df_origine['Classification'].apply(lambda x: 1 if x > 0 else 0)
if df_origine['Classification'].nunique() != 2:
    print("La colonne 'Classification' doit contenir exactement deux classes (0 et 1).")

df_majority = df_origine[df_origine.Classification == 0]
df_minority = df_origine[df_origine.Classification == 1]

if df_majority.empty or df_minority.empty:
    print("Il doit y avoir au moins un exemple dans chaque classe.")

df_minority_upsampled = resample(df_minority,
                                 replace=True,     # échantillonnage avec remplacement
                                 n_samples=len(df_majority),    # pour correspondre au nombre de la classe majoritaire
                                 random_state=123) # pour la reproductibilité

df_upsampled = pd.concat([df_majority, df_minority_upsampled])
# **Séparation des données en ensembles d'entraînement et de test**
X = df_upsampled.drop('Classification', axis=1)
y = df_upsampled['Classification']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

models = {
    "Random Forest": RandomForestClassifier(),
    # Ajouter d'autres modèles si nécessaire
}

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    #Afficher les résultats
    # print(f"--- {name} ---")
    # print(classification_report(y_test, y_pred))
    # print(confusion_matrix(y_test, y_pred))