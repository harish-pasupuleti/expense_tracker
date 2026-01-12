import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "expenses.csv")

def load_expenses():
    if not os.path.exists(DATA_PATH):
        return pd.DataFrame(columns=["date", "category", "amount"])
    return pd.read_csv(DATA_PATH)

def add_expense(date, category, amount):
    df = load_expenses()
    new_row = pd.DataFrame([[date, category, amount]],
                            columns=["date", "category", "amount"])
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(DATA_PATH, index=False)
