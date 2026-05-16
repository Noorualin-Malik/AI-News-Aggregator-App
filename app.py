import streamlit as st
from fetch_news import fetch_news
from filter_news import filter_article
from database import create_table, save_lead, get_all_leads

st.set_page_config(page_title="AI News Lead Aggregator")

st.title("🚀 Real-Time AI News Lead Aggregator")

create_table()

if st.button("Fetch & Analyze News"):

    news = fetch_news()

    if not news:
        st.error("No news articles fetched.")
    else:

        st.subheader("Fetched Articles")

        count = 0

        for article in news:

            st.markdown("---")

            st.write("### 📰", article["title"])

            st.write(article["description"])

            st.write("Source:", article["source"])

            with st.spinner("Analyzing with Gemini AI..."):

                is_relevant = filter_article(article)

            if is_relevant:

                st.success("✅ High-Value Lead Found")

                save_lead(article)

                count += 1

            else:

                st.warning("❌ Not Relevant")

        st.subheader("Final Result")

        st.success(f"{count} high-value leads saved!")

# SHOW SAVED LEADS

st.subheader("📌 Saved Leads")

leads = get_all_leads()

if leads:

    for lead in leads:

        st.markdown("---")

        st.write("###", lead[1])

        st.write(lead[2])

        st.write("Source:", lead[3])

        st.markdown(f"[Read Full Article]({lead[4]})")

else:

    st.info("No leads saved yet.")