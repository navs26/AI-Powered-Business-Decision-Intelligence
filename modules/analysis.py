import pandas as pd

def calculate_kpis(df):

    kpis = {}

    numeric_columns = df.select_dtypes(include="number").columns

    if "Sales" in df.columns:
        kpis["Total Sales"] = round(df["Sales"].sum(), 2)

    elif "Amount" in df.columns:
        kpis["Total Sales"] = round(df["Amount"].sum(), 2)

    if "Profit" in df.columns:
        kpis["Total Profit"] = round(df["Profit"].sum(), 2)

    if "Order ID" in df.columns:
        kpis["Total Orders"] = df["Order ID"].nunique()

    elif "Orders" in df.columns:
        kpis["Total Orders"] = df["Orders"].sum()

    if "Sales" in df.columns:
        kpis["Average Sales"] = round(df["Sales"].mean(), 2)

    elif "Amount" in df.columns:
        kpis["Average Sales"] = round(df["Amount"].mean(), 2)

    kpis["Total Records"] = len(df)

    return kpis