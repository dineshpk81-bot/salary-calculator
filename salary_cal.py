import streamlit as st

# Tax calculation function
def calculate_tax(salary):
    tax = 0
    if salary <= 400000:
        tax = 0
    elif salary <= 800000:
        tax = (salary - 400000) * 0.05
    elif salary <= 1200000:
        tax = (400000 * 0.05) + (salary - 800000) * 0.10
    elif salary <= 1600000:
        tax = (400000 * 0.05) + (400000 * 0.10) + (salary - 1200000) * 0.15
    elif salary <= 2000000:
        tax = (400000 * 0.05) + (400000 * 0.10) + (400000 * 0.15) + (salary - 1600000) * 0.20
    elif salary <= 2400000:
        tax = (400000 * 0.05) + (400000 * 0.10) + (400000 * 0.15) + (400000 * 0.20) + (salary - 2000000) * 0.25
    else:
        tax = (400000 * 0.05) + (400000 * 0.10) + (400000 * 0.15) + (400000 * 0.20) + (400000 * 0.25) + (salary - 2400000) * 0.30
    return tax

# Streamlit UI
st.title("💰 Salary Calculator")
st.write("Calculate your new salary after hike, variable pay, and tax deductions.")

current_package = st.number_input("Enter Current Package (₹)", min_value=0.0, step=10000.0)
hike_percentage = st.number_input("Enter Hike Percentage (optional)", min_value=0.0, step=0.1)
variable_percentage = st.number_input("Enter Variable Pay Percentage (optional)", min_value=0.0, step=0.1)

if st.button("Calculate"):
    # Hike calculation
    hike_amount = (current_package * hike_percentage) / 100
    new_package = current_package + hike_amount

    # Variable deduction
    variable_amount = (new_package * variable_percentage) / 100
    fixed_salary = new_package - variable_amount
    # Tax calculation
    tax_amount = calculate_tax(fixed_salary)
    final_salary = fixed_salary - tax_amount
    monthly_take_home = final_salary / 12

    st.subheader("📊 Salary Breakdown")
    st.write(f"**Current Package:** ₹{current_package:,.2f}")
    st.write(f"**Hike Amount:** ₹{hike_amount:,.2f}")
    st.write(f"**New Package (Before Variable):** ₹{new_package:,.2f}")
    st.write(f"**Variable Deduction:** ₹{variable_amount:,.2f}")
    st.write(f"**Fixed Salary (After Variable):** ₹{fixed_salary:,.2f}")
    st.write(f"**Tax Deduction:** ₹{tax_amount:,.2f}")
    st.write(f"**Final Package (After Tax):** ₹{final_salary:,.2f}")
    st.success(f"**Monthly Take-Home:** ₹{monthly_take_home:,.2f}")