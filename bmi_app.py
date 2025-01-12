import streamlit as st

def calculate_bmi(weight, height):
    """Calculate BMI using weight (kg) and height (cm)."""
    height_in_meters = height / 100  # Convert height to meters
    bmi = weight / (height_in_meters ** 2)
    return round(bmi, 2)

def bmi_category(bmi):
    """Return the BMI category based on the BMI value."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Streamlit UI
st.title("BMI Calculator")

# User inputs
weight = st.number_input("Enter your weight (kg):", min_value=1.0, format="%.2f")
height = st.number_input("Enter your height (cm):", min_value=1.0, format="%.2f")

# Calculate BMI when button is clicked
if st.button("Calculate BMI"):
    if weight > 0 and height > 0:
        bmi = calculate_bmi(weight, height)
        category = bmi_category(bmi)
        st.success(f"Your BMI is {bmi}, which falls under the category: {category}.")
    else:
        st.error("Please enter valid weight and height values.")

# Additional info
st.write("""
### BMI Categories:
- **Underweight**: BMI < 18.5
- **Normal weight**: BMI 18.5 - 24.9
- **Overweight**: BMI 25 - 29.9
- **Obesity**: BMI >= 30
""")
