import streamlit as st
import pandas as pd

from run import get_top_items, count_by_field


st.set_page_config(
    page_title="Career Compass",
    page_icon="🧭",
    layout="wide"
)
st.title("Career Compass")
st.write("Analyze job market trends from scraped job data.")

df = pd.read_csv('data/cleaned/jobs_cleaned.csv')

updated_jobs = df.to_dict(orient='records')

title_counts = count_by_field(updated_jobs, "title")
top_titles = get_top_items(title_counts, 5)
company_counts = count_by_field(updated_jobs  , "company")
top_companies = get_top_items(company_counts, 5)
location_counts = count_by_field(updated_jobs , "location")
top_locations = get_top_items(location_counts, 5)

col1, col2, col3 = st.columns(3)
col1.metric('Total Jobs', len(df))

if top_titles:
    col2.metric("Most Common Title", top_titles[0][0])

if top_locations:
    col3.metric("Most Common Location", top_locations[0][0])

st.subheader("Top Job Titles")
top_titles_df = pd.DataFrame(top_titles, columns=["Title", "Count"])
st.bar_chart(top_titles_df.set_index("Title"))

st.subheader("Top Job Company")
top_companies_df = pd.DataFrame(top_companies, columns=["Company", "Count"])
st.bar_chart(top_companies_df.set_index("Company"))

st.subheader("Top Job Location")
top_locations_df = pd.DataFrame(top_locations, columns=["Location", "Count"])
st.bar_chart(top_locations_df.set_index("Location"))