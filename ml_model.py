import pandas as pd
from expense_manager import load_expenses

def predict_next_month_expense():
    df = load_expenses()

    if df.empty:
        return 0

    total = df["amount"].sum()
    months = df["date"].nunique()

    avg_monthly = total / max(months, 1)
    prediction = avg_monthly * 1.1

    return round(prediction, 2)
