
import streamlit as st
import pandas as pd
import plotly.express as px

from modules.data_cleaning import clean_data
from modules.analysis import calculate_kpis
from modules.ai_insights import generate_insights
from modules.recommendations import generate_recommendations

st.set_page_config(
    page_title="AI-Powered Business Decision Intelligence Platform",
    page_icon="BI",
    layout="wide"
)
st.markdown("""
<style>
.stApp {
    background-color: #F4F7FB;
    color: #334155;
}

[data-testid="stMetric"] {
    background-color: #FFFFFF;
    border: 1px solid #DCE5F0;
    border-radius: 12px;
    padding: 15px;
}

h1 {
    color: #1E3A5F;
}

h2, h3 {
    color: #1E3A5F;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="padding: 10px 0 20px 0;">
    <h1 style="font-size: 36px; color: #60A5FA;">
        Business Intelligence Dashboard
    </h1>
    <p style="color: #94A3B8; font-size: 16px;">
        AI-Powered Analytics | Data-Driven Decisions | Business Growth
    </p>
</div>
""", unsafe_allow_html=True)
st.caption("Transform raw business data into actionable decisions.")

st.sidebar.markdown("""
<h2 style="color:#60A5FA;">Business Intelligence</h2>
""", unsafe_allow_html=True)
st.sidebar.markdown(
    "<p style='color:#94A3B8;'>Upload your business dataset to get started.</p>",
    unsafe_allow_html=True
)

uploaded_file = st.sidebar.file_uploader(
    "Choose your business dataset",
    type=["csv", "xlsx"]
)

st.write("Welcome to your Business Intelligence Dashboard.")

if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        cleaned_df = clean_data(df)
        

        st.success("Dataset uploaded and cleaned successfully!")

        st.subheader("Dataset Preview")
        st.dataframe(cleaned_df.head(10), use_container_width=True)

        st.subheader("Dataset Information")

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Rows", len(cleaned_df))
        col2.metric("Total Columns", len(cleaned_df.columns))
        col3.metric("Duplicate Rows Removed", len(df) - len(cleaned_df))

        st.subheader("Business KPIs")

        kpis = calculate_kpis(cleaned_df)

        cols = st.columns(4)

        for i, (name, value) in enumerate(kpis.items()):
            cols[i % 4].metric(name, value)

        st.subheader("AI-Generated Business Insights")

        insights = generate_insights(cleaned_df)

        for insight in insights:
            st.info(insight)

        st.subheader("Business Recommendations")

        recommendations = generate_recommendations(cleaned_df)

        for recommendation in recommendations:
            st.success(recommendation)

            

        st.subheader("Business Data Visualization")
        st.markdown("""
<style>
.js-plotly-plot {
    border-radius: 12px;
    overflow: hidden;
}
</style>
""", unsafe_allow_html=True)

        numeric_columns = cleaned_df.select_dtypes(
            include="number"
        ).columns.tolist()

        if len(numeric_columns) > 0:

            selected_column = st.selectbox(
                "Select a metric to visualize",
                numeric_columns
            )

            fig = px.histogram(
                cleaned_df,
                x=selected_column,
                title=f"Distribution of {selected_column}"
            )

            st.plotly_chart(fig, use_container_width=True)

        else:
            st.warning("No numeric columns available for visualization.")

        # Sales by Region
        if "Region" in cleaned_df.columns and "Sales" in cleaned_df.columns:

            sales_by_region = cleaned_df.groupby(
                "Region", as_index=False
            )["Sales"].sum()

            fig_region = px.bar(
                sales_by_region,
                x="Region",
                y="Sales",
                color="Region",
                title="Sales by Region",
                text_auto=True
            )
            fig_region.update_traces(textposition="outside")
            fig_region.update_layout(
            xaxis_title="Region",
            yaxis_title="Total Sales",
            template="plotly_white"
)


            st.plotly_chart(
                fig_region,
                use_container_width=True,
                key="sales_region_chart"
            )

        # Sales by Product
        if "Product" in cleaned_df.columns and "Sales" in cleaned_df.columns:

            sales_by_product = cleaned_df.groupby(
                "Product", as_index=False
            )["Sales"].sum()

            fig_product = px.bar(
                sales_by_product,
                x="Product",
                y="Sales",
                color="Product",
                title="Sales by Product",
                text_auto=True
            )
            fig_product.update_traces(textposition="outside")
            fig_product.update_layout(
            xaxis_title="Product",
            yaxis_title="Total Sales",
            template="plotly_white"
)

            st.plotly_chart(
                fig_product,
                use_container_width=True,
                key="sales_product_chart"
            )

        # Profit by Region
        if "Region" in cleaned_df.columns and "Profit" in cleaned_df.columns:

            profit_by_region = cleaned_df.groupby(
                "Region", as_index=False
            )["Profit"].sum()

            fig_profit = px.bar(
                profit_by_region,
                x="Region",
                y="Profit",
                color="Region",
                title="Profit by Region",
                text_auto=True
            )
            fig_profit.update_traces(textposition="outside")
            fig_profit.update_layout(
            xaxis_title="Region",
            yaxis_title="Total Profit",
            template="plotly_white"
)

            st.plotly_chart(
                fig_profit,
                use_container_width=True,
                key="profit_region_chart"
            )

        st.subheader("Download Cleaned Dataset")

        csv_data = cleaned_df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="Download Cleaned CSV",
            data=csv_data,
            file_name="cleaned_business_data.csv",
            mime="text/csv"
        )

    except Exception as e:
        st.error(f"Error processing dataset: {e}")
