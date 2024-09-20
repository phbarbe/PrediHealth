import streamlit as st
import base64
from streamlit_option_menu import option_menu

# Importing the different diseases
import breast_cancer
import diabetes
import kidney_disease
import liver_disease
import heart_disease

st.set_page_config(
    page_title="Predictions de maladies",
    page_icon="images/Logo_PrediHealth.png",
    layout="wide",
    initial_sidebar_state="expanded",
)

# mettre une image en fond d'écran
def get_base64(bin_file):
    with open(bin_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = (
        """
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    """
        % bin_str
    )
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background("images/background.png")

with st.sidebar:
    st.sidebar.image(
        "images/Logo_PrediHealth.png",
        width=250,
    )
    selected = option_menu(
        menu_title=None,
        options=[
            "select :",
            "Breast Cancer",
            "Diabetes",
            "Kidney Disease",
            "Liver Disease",
            "Heart Disease",
        ],
        styles={
            "container": {
                "padding": "0!important",
                "background-color": "#b5b5b5",
                "border-radius": "1px",
            },
            "nav-link": {
                "font-size": "12px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
                "color": "#ffffff",
            },
            "nav-link-selected": {"background-color": "#5f5f5f"},
        },
    )

def local_css(css_file_path):
    with open(css_file_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# Afficher la page correspondante si une option est sélectionnée
if selected == "Breast Cancer":
    breast_cancer.show()
elif selected == "Diabetes":
    diabetes.show()
elif selected == "Kidney Disease":
    kidney_disease.show()
elif selected == "Liver Disease":
    liver_disease.show()
elif selected == "Heart Disease":
    heart_disease.show()
elif selected == "select :":
    multi = """
<h1 style='text-align: center; color: #34495E;'>Welcome to our disease prediction app!</h1>
<h3 style='text-align: center; color: #74818E;'>This app is designed to predict the likelihood of a patient having a particular disease based on their medical history.</h3>
<h2 style='text-align: center; color: #34495E;'>Please select a disease from the sidebar to get started.</h2>
<h4 style='text-align: center; color: #74818E;'>Disclaimer: This app is for educational purposes only and does not replace a professional medical diagnosis.</h4>
"""
    st.markdown(multi, unsafe_allow_html=True)

