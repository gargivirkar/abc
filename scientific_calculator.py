import streamlit as st
import math

st.title("🧪 Scientific Calculator")

# --- Input Section ---
num = st.number_input("Enter a number:", format="%.8f")

operation = st.selectbox(
    "Select an operation:",
    [
        "Square",
        "Cube",
        "Square Root",
        "Log (base 10)",
        "Natural Log (ln)",
        "Sine",
        "Cosine",
        "Tangent",
        "Power (x^y)"
    ]
)

if operation == "Power (x^y)":
    num2 = st.number_input("Enter exponent (y):", format="%.4f")
else:
    num2 = None

# --- Calculation ---
if st.button("Calculate"):
    try:
        if operation == "Square":
            result = num ** 2

        elif operation == "Cube":
            result = num ** 3

        elif operation == "Square Root":
            if num < 0:
                result = "Error: Cannot take square root of negative number!"
            else:
                result = math.sqrt(num)

        elif operation == "Log (base 10)":
            if num <= 0:
                result = "Error: log10 not defined for <= 0!"
            else:
                result = math.log10(num)

        elif operation == "Natural Log (ln)":
            if num <= 0:
                result = "Error: ln not defined for <= 0!"
            else:
                result = math.log(num)

        elif operation == "Sine":
            result = math.sin(math.radians(num))

        elif operation == "Cosine":
            result = math.cos(math.radians(num))

        elif operation == "Tangent":
            result = math.tan(math.radians(num))

        elif operation == "Power (x^y)":
            result = math.pow(num, num2)

        st.success(f"Result: {result}")

    except Exception as e:
        st.error(f"Error: {e}")
