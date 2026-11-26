def generate_recommendations(df):
    recommendations = []

    # Sales by region
    if "Region" in df.columns and "Sales" in df.columns:
        region_sales = df.groupby("Region")["Sales"].sum()
        best_region = region_sales.idxmax()

        recommendations.append(
            f"Your strongest sales region is {best_region}. "
            "Consider investing more marketing efforts in this region."
        )

    # Sales by product
    if "Product" in df.columns and "Sales" in df.columns:
        product_sales = df.groupby("Product")["Sales"].sum()
        best_product = product_sales.idxmax()

        recommendations.append(
            f"{best_product} is your top-selling product. "
            "Consider maintaining sufficient stock to meet demand."
        )

    # Profit analysis
    if "Region" in df.columns and "Profit" in df.columns:
        region_profit = df.groupby("Region")["Profit"].sum()
        best_profit_region = region_profit.idxmax()

        recommendations.append(
            f"{best_profit_region} generates the highest total profit. "
            "Focus on sustaining profitability in this region."
        )

    if not recommendations:
        recommendations.append(
            "Upload a sales dataset containing Region, Product, Sales, or Profit "
            "columns to receive business recommendations."
        )

    return recommendations