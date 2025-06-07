import streamlit as st
import pandas as pd
import requests


st.set_page_config(page_title="IT Companies in Noida", layout="wide")
st.title("IT Company Scraper (Google Maps)")

if st.button("Scrape IT Companies"):
    with st.spinner("Scraping data from Google Maps..."):
        try:
            response = requests.get("http://127.0.0.1:5000/scrape")
        except Exception as e:
            st.error(f"Error connecting to backend: {e}")
            st.stop()

    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data, columns=["Company Name", "Phone Number", "Address"])
        st.success(f"Scraping completed! Found {len(data)} companies.")
        st.dataframe(df)

        st.download_button(
            label="Download CSV",
            data=df.to_csv(index=False),
            file_name="it_companies_noida.csv",
            mime="text/csv"
        )
    else:
        st.error("Failed to scrape data. Please check the backend.")
