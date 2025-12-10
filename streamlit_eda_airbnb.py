
import streamlit as st
from eda_air_bnb import (
    load_data,
    price_distribution,
    room_type_distribution,
    listings_by_neighbourhood,
    price_vs_room_type,
    reviews_over_time,
    correlation_heatmap,
    geographical_dotted_plot
)

st.set_page_config(
    page_title="Airbnb EDA Dashboard",
    layout="wide",
)

st.markdown(
    """
    <h1 style='text-align:center; color:#E74C3C;'>Airbnb Data Analysis Dashboard</h1>
    <p style='text-align:center; font-size:18px;'>
    Explore insights about Airbnb listings including pricing, room types, neighbourhood trends, and customer reviews.
    </p>
    <hr>
    """,
    unsafe_allow_html=True,
)

st.sidebar.header("Navigation Panel")
menu = [
    "Distribution of Listing Prices",
    "Room Type Distribution",
    "Listings by Neighbourhood",
    "Price vs Room Type",
    "Number of Reviews Over Time",
    "Correlation Heatmap",
    "Geographical Distribution Plot"
]
choice = st.sidebar.radio("Select Analysis", menu)

st.sidebar.subheader("Data Source")
st.sidebar.info("Using the local dataset: 'compressed_data.csv'")
df = load_data("compressed_data.csv")

if choice == "Distribution of Listing Prices":
    st.subheader("Distribution of Listing Prices")
    st.pyplot(price_distribution(df))

elif choice == "Room Type Distribution":
    st.subheader("Room Type Distribution")
    st.pyplot(room_type_distribution(df))

elif choice == "Listings by Neighbourhood":
    st.subheader("Listings by Neighbourhood Group")
    st.pyplot(listings_by_neighbourhood(df))

elif choice == "Price vs Room Type":
    st.subheader("Price vs Room Type")
    st.pyplot(price_vs_room_type(df))

elif choice == "Number of Reviews Over Time":
    st.subheader("Number of Reviews Over Time")
    st.pyplot(reviews_over_time(df))

elif choice == "Correlation Heatmap":
    st.subheader("Feature Correlation Heatmap")
    st.pyplot(correlation_heatmap(df))

elif choice == "Geographical Distribution Plot":
    st.subheader("Geographical Distribution of Airbnb Listings by Room Type")
    st.pyplot(geographical_dotted_plot(df))

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center; font-size:14px;'>Developed using Streamlit and Seaborn</p>",
    unsafe_allow_html=True,
)
