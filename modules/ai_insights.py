def generate_insights(df):
    insights = []

    # Sales insights
    if "Sales" in df.columns:
        total_sales = df["Sales"].sum()
        average_sales = df["Sales"].mean()

        insights.append(
            f"Total sales recorded: {total_sales:.2f}"
        )

        if total_sales > 0:
            insights.append(
                "Business sales are generating positive revenue."
            )

        if average_sales > 0:
            insights.append(
                f"Average sales per record: {average_sales:.2f}"
            )

    # Profit insights
    if "Profit" in df.columns:
        total_profit = df["Profit"].sum()

        if total_profit > 0:
            insights.append(
                "The business is operating with an overall positive profit."
            )
        elif total_profit < 0:
            insights.append(
                "The dataset indicates an overall loss. Review expenses and pricing."
            )
        else:
            insights.append(
                "Overall profit is currently zero."
            )

    # Dataset insights
    insights.append(
        f"The uploaded dataset contains {len(df)} records."
    )

    insights.append(
        f"The dataset contains {len(df.columns)} columns."
    )

    return insights