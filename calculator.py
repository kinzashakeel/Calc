import streamlit as st

# Set the title of the app
st.title("Simple Calculator")

# Create input fields for the two numbers
num1 = st.number_input("Enter the first number")
num2 = st.number_input("Enter the second number")

# Create radio buttons for the operation selection
operation = st.radio("Select an operation", ("Add", "Subtract", "Multiply", "Divide"))

# Function to perform the calculation
def calculate(num1, num2, operation):
    if operation == "Add":
        return num1 + num2
    elif operation == "Subtract":
        return num1 - num2
    elif operation == "Multiply":
        return num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"

# Button to perform the calculation
if st.button("Calculate"):
    result = calculate(num1, num2, operation)
    st.write(f"The result is: {result}")

