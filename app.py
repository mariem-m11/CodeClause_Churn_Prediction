import streamlit as st
import pandas as pd
import pickle

# Load the trained logistic regression model from .sav file
model = pickle.load(open('trained_model.sav', 'rb'))

# Create the Streamlit app
def main():
    # Set the app title
    st.title("Churn Prediction App")

    # Create input fields for user to enter data
    tenure = st.slider("Tenure", min_value=0, max_value=100, value=50)
    monthly_charges = st.slider("Monthly Charges", min_value=0.0, max_value=200.0, value=100.0)
    total_charges = st.slider("Total Charges", min_value=0.0, max_value=5000.0, value=2500.0)
    fiber_optic_internet = st.selectbox("Fiber Optic Internet", ["No", "Yes"])
    contract_monthly = st.selectbox("Contract (Monthly)", ["No", "Yes"])

    # Create a DataFrame with the user input
    input_data = pd.DataFrame({
        "tenure": [tenure],
        "MonthlyCharges": [monthly_charges],
        "TotalCharges": [total_charges],
        "InternetService_Fiber optic": [1 if fiber_optic_internet == "Yes" else 0],
        "Contract_Month-to-month": [1 if contract_monthly == "Yes" else 0]
    })

    # Make a prediction using the trained model
    prediction = model.predict(input_data)

    # Display the prediction to the user
    if prediction[0] == 0:
        st.markdown("Prediction: **Not Churned**")
    else:
        st.markdown("Prediction: **Churned**")

# Run the app
if __name__ == "__main__":
    main()
