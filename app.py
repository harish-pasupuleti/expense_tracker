import streamlit as st
import pandas as pd
from expense_manager import add_expense, load_expenses
from chatbot import chatbot_response

# ---------- Page Config ----------
st.set_page_config(
    page_title="AI Expense Tracker",
    layout="centered"
)

st.title("💰 AI Expense Tracker with Chatbot")

# ---------- Add Expense ----------
st.subheader("➕ Add Expense")

date = st.date_input("Date")
category = st.text_input("Category (Food, Travel, Rent, etc.)")
amount = st.number_input("Amount (₹)", min_value=0.0, step=1.0)

if st.button("Add Expense"):
    if category.strip() == "":
        st.warning("Please enter a category")
    else:
        add_expense(str(date), category, amount)
        st.success("✅ Expense added successfully")

# ---------- Show Expenses ----------
st.subheader("📊 Expense Records")

df = load_expenses()

if df.empty:
    st.info("No expenses added yet.")
else:
    st.dataframe(df, use_container_width=True)

    # ---------- Monthly Trend ----------
    st.subheader("📅 Monthly Expense Trend")

    df["date"] = pd.to_datetime(df["date"])
    monthly_expense = df.groupby(df["date"].dt.to_period("M"))["amount"].sum()
    st.line_chart(monthly_expense)

# ---------- Chatbot ----------
st.subheader("🤖 Expense Chatbot")

st.caption("Try asking: total expense, highest category, average expense, predict next month")

user_input = st.text_input("Ask your question:")

if user_input:
    response = chatbot_response(user_input)
    st.info(response)
