import streamlit as st
import pandas as pd

# Chargement des données
url = 'https://raw.githubusercontent.com/MaskiVal/DataSets/main/cancer_breast.csv'
breast_cancer = pd.read_csv(url)

def create_number_input(label, df, column, min_value=0.0, format="%.6f"):
    value = df[df['diagnosis'] == 'B'].drop(columns=["id", "Unnamed: 32","diagnosis"]).median()[column]
    return st.number_input(label, min_value=min_value, value=value, format=format)

# def pour calcul du premier quartile
def Q1_benin(df, column):
    return df[df['diagnosis'] == 'B'].drop(columns=["id", "Unnamed: 32","diagnosis"]).quantile(0.25)[column]

# def pour calcul de la médiane
def median_benin(df, column):
    return df[df['diagnosis'] == 'B'].drop(columns=["id", "Unnamed: 32","diagnosis"]).median()[column]

# def pour calcul du troisième quartile
def Q3_benin(df, column):
    return df[df['diagnosis'] == 'B'].drop(columns=["id", "Unnamed: 32","diagnosis"]).quantile(0.75)[column]


def show():
    st.title("Breast Cancer Prediction")

    st.header("Enter the following data:")

    # Input fields for the mean values
    st.subheader("Mean Values")
    radius_mean = create_number_input("Radius Mean", breast_cancer, "radius_mean", format="%.4f")
    st.write(f"25% < {Q1_benin(breast_cancer, 'radius_mean')}")
    st.write(f"50% < {median_benin(breast_cancer, 'radius_mean')}")
    st.write(f"75% < {Q3_benin(breast_cancer, 'radius_mean')}")
    
    texture_mean = create_number_input("Texture Mean", breast_cancer, "texture_mean", format="%.4f")
    st.write(f"25% < {Q1_benin(breast_cancer, 'texture_mean')}")
    st.write(f"50% < {median_benin(breast_cancer, 'texture_mean')}")
    st.write(f"75% < {Q3_benin(breast_cancer, 'texture_mean')}")
    
    perimeter_mean = create_number_input("Perimeter Mean", breast_cancer, "perimeter_mean", format="%.4f")
    st.write(f"25% < {Q1_benin(breast_cancer, 'perimeter_mean')}")
    st.write(f"50% < {median_benin(breast_cancer, 'perimeter_mean')}")
    st.write(f"75% < {Q3_benin(breast_cancer, 'perimeter_mean')}")
    
    area_mean = create_number_input("Area Mean", breast_cancer, "area_mean", format="%.4f")
    st.write(f"25% < {Q1_benin(breast_cancer, 'area_mean')}")
    st.write(f"50% < {median_benin(breast_cancer, 'area_mean')}")
    st.write(f"75% < {Q3_benin(breast_cancer, 'area_mean')}")
    
    smoothness_mean = create_number_input("Smoothness Mean", breast_cancer, "smoothness_mean")
    st.write(f"25% < {Q1_benin(breast_cancer, 'smoothness_mean')}")
    st.write(f"50% < {median_benin(breast_cancer, 'smoothness_mean')}")
    st.write(f"75% < {Q3_benin(breast_cancer, 'smoothness_mean')}")

    compactness_mean = create_number_input("Compactness Mean", breast_cancer, "compactness_mean")
    st.write(f"25% < {Q1_benin(breast_cancer, 'compactness_mean')}")
    st.write(f"50% < {median_benin(breast_cancer, 'compactness_mean')}")
    st.write(f"75% < {Q3_benin(breast_cancer, 'compactness_mean')}")
    
    concavity_mean = create_number_input("Concavity Mean", breast_cancer, "concavity_mean")
    st.write(f"25% < {Q1_benin(breast_cancer, 'concavity_mean')}")
    st.write(f"50% < {median_benin(breast_cancer, 'concavity_mean')}")
    st.write(f"75% < {Q3_benin(breast_cancer, 'concavity_mean')}")
    
    concave_points_mean = create_number_input("Concave Points Mean", breast_cancer, "concave points_mean")
    st.write(f"25% < {Q1_benin(breast_cancer, 'concave points_mean')}")
    st.write(f"50% < {median_benin(breast_cancer, 'concave points_mean')}")
    st.write(f"75% < {Q3_benin(breast_cancer, 'concave points_mean')}")
    
    symmetry_mean = create_number_input("Symmetry Mean", breast_cancer, "symmetry_mean")
    st.write(f"25% < {Q1_benin(breast_cancer, 'symmetry_mean')}")
    st.write(f"50% < {median_benin(breast_cancer, 'symmetry_mean')}")
    st.write(f"75% < {Q3_benin(breast_cancer, 'symmetry_mean')}")
    
    fractal_dimension_mean = create_number_input("Fractal Dimension Mean", breast_cancer, "fractal_dimension_mean")
    st.write(f"25% < {Q1_benin(breast_cancer, 'fractal_dimension_mean')}")
    st.write(f"50% < {median_benin(breast_cancer, 'fractal_dimension_mean')}")
    st.write(f"75% < {Q3_benin(breast_cancer, 'fractal_dimension_mean')}")

    # Input fields for the standard error values
    st.subheader("Standard Error Values")
    radius_se = create_number_input("Radius SE", breast_cancer, "radius_se")
    st.write(f"25% < {Q1_benin(breast_cancer, 'radius_se')}")
    st.write(f"50% < {median_benin(breast_cancer, 'radius_se')}")
    st.write(f"75% < {Q3_benin(breast_cancer, 'radius_se')}")
    texture_se = create_number_input("Texture SE", breast_cancer, "texture_se")
    st.write(f"25% < {Q1_benin(breast_cancer, 'texture_se')}")
    st.write(f"50% < {median_benin(breast_cancer, 'texture_se')}")
    st.write(f"75% < {Q3_benin(breast_cancer, 'texture_se')}")
    perimeter_se = create_number_input("Perimeter SE", breast_cancer, "perimeter_se")
    st.write(f"25% < {Q1_benin(breast_cancer, 'perimeter_se')}")
    st.write(f"50% < {median_benin(breast_cancer, 'perimeter_se')}")
    st.write(f"75% < {Q3_benin(breast_cancer, 'perimeter_se')}")
    area_se = create_number_input("Area SE", breast_cancer, "area_se", format="%.4f")
    st.write(f"25% < {Q1_benin(breast_cancer, 'area_se')}")
    st.write(f"50% < {median_benin(breast_cancer, 'area_se')}")
    st.write(f"75% < {Q3_benin(breast_cancer, 'area_se')}")
    smoothness_se = create_number_input("Smoothness SE", breast_cancer, "smoothness_se")
    st.write(f"25% < {Q1_benin(breast_cancer, 'smoothness_se')}")
    st.write(f"50% < {median_benin(breast_cancer, 'smoothness_se')}")
    st.write(f"75% < {Q3_benin(breast_cancer, 'smoothness_se')}")

    compactness_se = create_number_input("Compactness SE", breast_cancer, "compactness_se")
    st.write(f"25% < {Q1_benin(breast_cancer, 'compactness_se')}")
    st.write(f"50% < {median_benin(breast_cancer, 'compactness_se')}")
    st.write(f"75% < {Q3_benin(breast_cancer, 'compactness_se')}")
    concavity_se = create_number_input("Concavity SE", breast_cancer, "concavity_se")
    st.write(f"25% < {Q1_benin(breast_cancer, 'concavity_se')}")
    st.write(f"50% < {median_benin(breast_cancer, 'concavity_se')}")
    st.write(f"75% < {Q3_benin(breast_cancer, 'concavity_se')}")
    concave_points_se = create_number_input("Concave Points SE", breast_cancer, "concave points_se")
    st.write(f"25% < {Q1_benin(breast_cancer, 'concave points_se')}")
    st.write(f"50% < {median_benin(breast_cancer, 'concave points_se')}")
    st.write(f"75% < {Q3_benin(breast_cancer, 'concave points_se')}")
    symmetry_se = create_number_input("Symmetry SE", breast_cancer, "symmetry_se")
    st.write(f"25% < {Q1_benin(breast_cancer, 'symmetry_se')}")
    st.write(f"50% < {median_benin(breast_cancer, 'symmetry_se')}")
    st.write(f"75% < {Q3_benin(breast_cancer, 'symmetry_se')}")
    fractal_dimension_se = create_number_input("Fractal Dimension SE", breast_cancer, "fractal_dimension_se")
    st.write(f"25% < {Q1_benin(breast_cancer, 'fractal_dimension_se')}")
    st.write(f"50% < {median_benin(breast_cancer, 'fractal_dimension_se')}")
    st.write(f"75% < {Q3_benin(breast_cancer, 'fractal_dimension_se')}")

    # Input fields for the worst values
    st.subheader("Worst Values")
    radius_worst = create_number_input("Radius Worst", breast_cancer, "radius_worst", format="%.4f")
    st.write(f"25% < {Q1_benin(breast_cancer, 'radius_worst')}")
    st.write(f"50% < {median_benin(breast_cancer, 'radius_worst')}")
    st.write(f"75% < {Q3_benin(breast_cancer, 'radius_worst')}")
    texture_worst = create_number_input("Texture Worst", breast_cancer, "texture_worst", format="%.4f")
    st.write(f"25% < {Q1_benin(breast_cancer, 'texture_worst')}")
    st.write(f"50% < {median_benin(breast_cancer, 'texture_worst')}")
    st.write(f"75% < {Q3_benin(breast_cancer, 'texture_worst')}")
    perimeter_worst = create_number_input("Perimeter Worst", breast_cancer, "perimeter_worst", format="%.4f")
    st.write(f"25% < {Q1_benin(breast_cancer, 'perimeter_worst')}")
    st.write(f"50% < {median_benin(breast_cancer, 'perimeter_worst')}")
    st.write(f"75% < {Q3_benin(breast_cancer, 'perimeter_worst')}")
    area_worst = create_number_input("Area Worst", breast_cancer, "area_worst", format="%.4f")
    st.write(f"25% < {Q1_benin(breast_cancer, 'area_worst')}")
    st.write(f"50% < {median_benin(breast_cancer, 'area_worst')}")
    st.write(f"75% < {Q3_benin(breast_cancer, 'area_worst')}")
    smoothness_worst = create_number_input("Smoothness Worst", breast_cancer, "smoothness_worst")
    st.write(f"25% < {Q1_benin(breast_cancer, 'smoothness_worst')}")
    st.write(f"50% < {median_benin(breast_cancer, 'smoothness_worst')}")
    st.write(f"75% < {Q3_benin(breast_cancer, 'smoothness_worst')}")
    compactness_worst = create_number_input("Compactness Worst", breast_cancer, "compactness_worst")
    st.write(f"25% < {Q1_benin(breast_cancer, 'compactness_worst')}")
    st.write(f"50% < {median_benin(breast_cancer, 'compactness_worst')}")
    st.write(f"75% < {Q3_benin(breast_cancer, 'compactness_worst')}")
    concavity_worst = create_number_input("Concavity Worst", breast_cancer, "concavity_worst")
    st.write(f"25% < {Q1_benin(breast_cancer, 'concavity_worst')}")
    st.write(f"50% < {median_benin(breast_cancer, 'concavity_worst')}")
    st.write(f"75% < {Q3_benin(breast_cancer, 'concavity_worst')}")
    concave_points_worst = create_number_input("Concave Points Worst", breast_cancer, "concave points_worst")
    st.write(f"25% < {Q1_benin(breast_cancer, 'concave points_worst')}")
    st.write(f"50% < {median_benin(breast_cancer, 'concave points_worst')}")
    st.write(f"75% < {Q3_benin(breast_cancer, 'concave points_worst')}")
    symmetry_worst = create_number_input("Symmetry Worst", breast_cancer, "symmetry_worst")
    st.write(f"25% < {Q1_benin(breast_cancer, 'symmetry_worst')}")
    st.write(f"50% < {median_benin(breast_cancer, 'symmetry_worst')}")
    st.write(f"75% < {Q3_benin(breast_cancer, 'symmetry_worst')}")
    fractal_dimension_worst = create_number_input("Fractal Dimension Worst", breast_cancer, "fractal_dimension_worst")
    st.write(f"25% < {Q1_benin(breast_cancer, 'fractal_dimension_worst')}")
    st.write(f"50% < {median_benin(breast_cancer, 'fractal_dimension_worst')}")
    st.write(f"75% < {Q3_benin(breast_cancer, 'fractal_dimension_worst')}")

    # Add a submit button
    if st.button("Submit"):
        st.write("Data submitted successfully!")
        # Add the code for prediction or further processing here

if __name__ == "__main__":
    show()
