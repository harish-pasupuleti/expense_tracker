from expense_manager import load_expenses
import pandas as pd

def chatbot_response(user_input):
    user_input = user_input.lower()
    df = load_expenses()

    if df.empty:
        return "No expenses recorded yet."

    # TOTAL EXPENSE
    if "total" in user_input:
        total = df["amount"].sum()
        return f"Your total expense is ₹{total}"

    # HIGHEST CATEGORY
    elif "highest" in user_input or "most" in user_input:
        category = df.groupby("category")["amount"].sum().idxmax()
        return f"You spend the most on {category}"

    # AVERAGE EXPENSE
    elif "average" in user_input:
        avg = df["amount"].mean()
        return f"Your average expense is ₹{avg:.2f}"

    # PREDICTION (simple logic)
    elif "predict" in user_input or "next month" in user_input:
        monthly = df["amount"].sum()
        return f"Next month estimated expense: ₹{monthly * 1.1:.2f}"

    else:
        return "I can help with total, highest category, average, and prediction."
