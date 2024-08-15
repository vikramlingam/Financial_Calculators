import streamlit as st
import plotly.graph_objs as go

# Function to create an interactive plot
def create_interactive_plot(x, y, title, xlabel, ylabel):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines+markers', name=title))
    fig.update_layout(title=title, xaxis_title=xlabel, yaxis_title=ylabel)
    st.plotly_chart(fig)

# Lumpsum + SIP Calculator
def lumpsum_sip_calculator():
    st.title("Lumpsum + SIP Calculator")
    
    # Inputs
    lumpsum_investment = st.number_input("Lumpsum Investment Amount (₹)", value=100000, min_value=0)
    monthly_sip = st.number_input("Monthly SIP Amount (₹)", value=1000, min_value=0)
    annual_rate = st.number_input("Expected Annual Return Rate (%)", value=12.0, min_value=0.0, step=0.1)
    investment_period = st.number_input("Investment Period (Years)", value=10, min_value=1)
    
    # Calculation
    months = investment_period * 12
    monthly_rate = annual_rate / 12 / 100
    
    # Future Value of Lumpsum with monthly compounding
    future_value_lumpsum = lumpsum_investment * (1 + annual_rate / 100) ** investment_period
    
    # Future Value of SIP with monthly contributions
    future_value_sip = monthly_sip * (((1 + monthly_rate) ** months - 1) / monthly_rate) * (1 + monthly_rate)
    
    # Total Future Value
    total_future_value = future_value_lumpsum + future_value_sip
    
    # Display Results
    st.write(f"Future Value of Lumpsum: ₹{future_value_lumpsum:,.2f}")
    st.write(f"Future Value of SIP: ₹{future_value_sip:,.2f}")
    st.write(f"Total Future Value: ₹{total_future_value:,.2f}")
    
    # Plotting the growth over time
    months_range = list(range(1, months + 1))
    lumpsum_values = [lumpsum_investment * (1 + monthly_rate) ** m for m in months_range]
    sip_values = [monthly_sip * (((1 + monthly_rate) ** m - 1) / monthly_rate) * (1 + monthly_rate) for m in months_range]
    total_values = [l + s for l, s in zip(lumpsum_values, sip_values)]
    
    create_interactive_plot(months_range, total_values, "Lumpsum + SIP Growth Over Time", "Months", "Investment Value (₹)")

# SIP Calculator
def sip_calculator():
    st.title("SIP Calculator")
    monthly_sip = st.number_input("Monthly SIP Amount (₹)", value=1000, min_value=0)
    annual_rate = st.number_input("Expected Annual Return Rate (%)", value=12.0, min_value=0.0, step=0.1)
    investment_period = st.number_input("Investment Period (Years)", value=10, min_value=1)

    months = investment_period * 12
    monthly_rate = annual_rate / 12 / 100
    
    future_value_sip = monthly_sip * (((1 + monthly_rate) ** months - 1) / monthly_rate) * (1 + monthly_rate)
    
    st.write(f"Future Value of SIP: ₹{future_value_sip:,.2f}")
    
    # Plotting the SIP growth over time
    months_range = list(range(1, months + 1))
    sip_values = [monthly_sip * (((1 + monthly_rate) ** m - 1) / monthly_rate) * (1 + monthly_rate) for m in months_range]
    
    create_interactive_plot(months_range, sip_values, "SIP Growth Over Time", "Months", "Investment Value (₹)")

# SIP Calculator with Step-Up
def sip_stepup_calculator():
    st.title("SIP Calculator with Step-Up")
    monthly_sip = st.number_input("Initial Monthly SIP Amount (₹)", value=1000, min_value=0)
    annual_rate = st.number_input("Expected Annual Return Rate (%)", value=12.0, min_value=0.0, step=0.1)
    step_up_rate = st.number_input("Annual Step-Up Rate (%)", value=5.0, min_value=0.0, step=0.1)
    investment_period = st.number_input("Investment Period (Years)", value=10, min_value=1)

    months = investment_period * 12
    monthly_rate = annual_rate / 12 / 100

    future_value_sip = 0
    current_sip = monthly_sip
    sip_values = []

    for i in range(1, months + 1):
        future_value_sip += current_sip * (1 + monthly_rate) ** (months - i + 1)
        if i % 12 == 0:
            current_sip *= (1 + step_up_rate / 100)
        sip_values.append(future_value_sip)

    st.write(f"Future Value of SIP with Step-Up: ₹{future_value_sip:,.2f}")

    # Plotting the SIP with step-up growth over time
    months_range = list(range(1, months + 1))
    
    create_interactive_plot(months_range, sip_values, "SIP with Step-Up Growth Over Time", "Months", "Investment Value (₹)")

# Lumpsum Calculator
def lumpsum_calculator():
    st.title("Lumpsum Calculator")
    lumpsum_investment = st.number_input("Lumpsum Investment Amount (₹)", value=100000, min_value=0)
    annual_rate = st.number_input("Expected Annual Return Rate (%)", value=12.0, min_value=0.0, step=0.1)
    investment_period = st.number_input("Investment Period (Years)", value=10, min_value=1)

    future_value_lumpsum = lumpsum_investment * (1 + annual_rate / 100) ** investment_period
    
    st.write(f"Future Value of Lumpsum: ₹{future_value_lumpsum:,.2f}")
    
    # Plotting the Lumpsum growth over time
    years_range = list(range(1, investment_period + 1))
    lumpsum_values = [lumpsum_investment * (1 + annual_rate / 100) ** y for y in years_range]
    
    create_interactive_plot(years_range, lumpsum_values, "Lumpsum Growth Over Time", "Years", "Investment Value (₹)")

# EMI Calculator
def emi_calculator():
    st.title("EMI Calculator")
    loan_amount = st.number_input("Loan Amount (₹)", value=500000, min_value=0)
    annual_rate = st.number_input("Annual Interest Rate (%)", value=8.5, min_value=0.0, step=0.1)
    loan_period = st.number_input("Loan Period (Years)", value=20, min_value=1)

    months = loan_period * 12
    monthly_rate = annual_rate / 12 / 100
    emi = loan_amount * monthly_rate * ((1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
    
    st.write(f"EMI: ₹{emi:,.2f} per month")
    
    # Plotting the EMI over time
    months_range = list(range(1, months + 1))
    principal_remaining = [loan_amount * ((1 + monthly_rate) ** months - (1 + monthly_rate) ** m) / ((1 + monthly_rate) ** months - 1) for m in months_range]
    
    create_interactive_plot(months_range, principal_remaining, "Principal Remaining Over Time", "Months", "Principal Remaining (₹)")

# EMI Calculator with Prepayments
def emi_prepayment_calculator():
    st.title("EMI Calculator with Prepayments")
    loan_amount = st.number_input("Loan Amount (₹)", value=500000, min_value=0)
    annual_rate = st.number_input("Annual Interest Rate (%)", value=8.5, min_value=0.0, step=0.1)
    loan_period = st.number_input("Loan Period (Years)", value=20, min_value=1)
    prepayment_amount = st.number_input("Prepayment Amount (₹)", value=100000, min_value=0)
    prepayment_year = st.number_input("Year of Prepayment", value=5, min_value=1, max_value=loan_period)

    months = loan_period * 12
    prepayment_month = prepayment_year * 12
    monthly_rate = annual_rate / 12 / 100

    emi = loan_amount * monthly_rate * ((1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
    principal_remaining = loan_amount * ((1 + monthly_rate) ** months - (1 + monthly_rate) ** prepayment_month) / ((1 + monthly_rate) ** months - 1)
    new_loan_amount = principal_remaining - prepayment_amount
    new_months = months - prepayment_month
    new_emi = new_loan_amount * monthly_rate * ((1 + monthly_rate) ** new_months) / ((1 + monthly_rate) ** new_months - 1)
    
    st.write(f"New EMI after Prepayment: ₹{new_emi:,.2f} per month")
    
    # Plotting the Principal remaining after prepayment
    months_range = list(range(prepayment_month + 1, months + 1))
    principal_remaining_post_prepayment = [new_loan_amount * ((1 + monthly_rate) ** (new_months - m)) / ((1 + monthly_rate) ** new_months - 1) for m in range(len(months_range))]
    
    create_interactive_plot(months_range, principal_remaining_post_prepayment, "Principal Remaining After Prepayment", "Months", "Principal Remaining (₹)")

# Sidebar for navigation
st.sidebar.title("Financial Calculators")
calculator = st.sidebar.selectbox("Select a Calculator", 
                                  ["Lumpsum + SIP Calculator",
                                   "SIP Calculator", 
                                   "SIP Calculator with Step-Up", 
                                   "Lumpsum Calculator", 
                                   "EMI Calculator", 
                                   "EMI Calculator with Prepayments"])

# Display the selected calculator
if calculator == "Lumpsum + SIP Calculator":
    lumpsum_sip_calculator()
elif calculator == "SIP Calculator":
    sip_calculator()
elif calculator == "SIP Calculator with Step-Up":
    sip_stepup_calculator()
elif calculator == "Lumpsum Calculator":
    lumpsum_calculator()
elif calculator == "EMI Calculator":
    emi_calculator()
elif calculator == "EMI Calculator with Prepayments":
    emi_prepayment_calculator()
