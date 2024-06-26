import streamlit as st

def show():
    st.title("Breast Cancer Prediction")

    st.header("Enter the following data:")

    # Input fields for the mean values
    st.subheader("Mean Values")
    radius_mean = st.number_input("Radius Mean", min_value=0.0, format="%.2f")
    texture_mean = st.number_input("Texture Mean", min_value=0.0, format="%.2f")
    perimeter_mean = st.number_input("Perimeter Mean", min_value=0.0, format="%.2f")
    area_mean = st.number_input("Area Mean", min_value=0.0, format="%.2f")
    smoothness_mean = st.number_input("Smoothness Mean", min_value=0.0, format="%.4f")
    compactness_mean = st.number_input("Compactness Mean", min_value=0.0, format="%.4f")
    concavity_mean = st.number_input("Concavity Mean", min_value=0.0, format="%.4f")
    concave_points_mean = st.number_input("Concave Points Mean", min_value=0.0, format="%.4f")
    symmetry_mean = st.number_input("Symmetry Mean", min_value=0.0, format="%.4f")
    fractal_dimension_mean = st.number_input("Fractal Dimension Mean", min_value=0.0, format="%.4f")

    # Input fields for the standard error values
    st.subheader("Standard Error Values")
    radius_se = st.number_input("Radius SE", min_value=0.0, format="%.4f")
    texture_se = st.number_input("Texture SE", min_value=0.0, format="%.4f")
    perimeter_se = st.number_input("Perimeter SE", min_value=0.0, format="%.4f")
    area_se = st.number_input("Area SE", min_value=0.0, format="%.4f")
    smoothness_se = st.number_input("Smoothness SE", min_value=0.0, format="%.4f")
    compactness_se = st.number_input("Compactness SE", min_value=0.0, format="%.4f")
    concavity_se = st.number_input("Concavity SE", min_value=0.0, format="%.4f")
    concave_points_se = st.number_input("Concave Points SE", min_value=0.0, format="%.4f")
    symmetry_se = st.number_input("Symmetry SE", min_value=0.0, format="%.4f")
    fractal_dimension_se = st.number_input("Fractal Dimension SE", min_value=0.0, format="%.4f")

    # Input fields for the worst values
    st.subheader("Worst Values")
    radius_worst = st.number_input("Radius Worst", min_value=0.0, format="%.2f")
    texture_worst = st.number_input("Texture Worst", min_value=0.0, format="%.2f")
    perimeter_worst = st.number_input("Perimeter Worst", min_value=0.0, format="%.2f")
    area_worst = st.number_input("Area Worst", min_value=0.0, format="%.2f")
    smoothness_worst = st.number_input("Smoothness Worst", min_value=0.0, format="%.4f")
    compactness_worst = st.number_input("Compactness Worst", min_value=0.0, format="%.4f")
    concavity_worst = st.number_input("Concavity Worst", min_value=0.0, format="%.4f")
    concave_points_worst = st.number_input("Concave Points Worst", min_value=0.0, format="%.4f")
    symmetry_worst = st.number_input("Symmetry Worst", min_value=0.0, format="%.4f")
    fractal_dimension_worst = st.number_input("Fractal Dimension Worst", min_value=0.0, format="%.4f")

    # Add a submit button
    if st.button("Submit"):
        st.write("Data submitted successfully!")
        # Add the code for prediction or further processing here

if __name__ == "__main__":
    show()
