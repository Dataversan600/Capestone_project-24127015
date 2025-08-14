import streamlit as st




import os
print("DIRECTORY:",os.listdir())

# Page title
st.title("Capestone Project OPEN LEARN 1.0, AUG 2025")

# Sidebar for navigation
st.sidebar.title("Home")
page = st.sidebar.radio("Go to", ["eda_notebook", "Classification Model", "Regression Model", "Unsupervised Model"])

# Import our all  notebooks
import eda_notebook
import unsupervised_notebook
import classification_notebook
import regression_notebook

# Page routing
if page == "eda_notebook":
   eda_notebook.run()
elif page == "classification_notebook":
    classification_notebook.run()
elif page == "regression_notebook":
    regression_notebook.run()
elif page == "unsupervised_notebook":
    unsupervised_notebook.run()

   
if __name__ == "__main__":
    # This runs only when executing app.py directly
    st.set_page_config(page_title="Rohith Varshan Capestone [24127015]", layout="wide")