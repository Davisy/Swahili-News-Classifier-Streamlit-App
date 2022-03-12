import streamlit as st
import requests as r
from langdetect import detect


# add banner image
st.header("Swahili News classifier App")
st.image("images/swahili-news.png")
st.subheader(
    """
A simple app to classify swahili news into different categories.
"""
)

# form to collect news content
my_form = st.form(key="news_form")
news = my_form.text_input("Input your swahili news content here")
submit = my_form.form_submit_button(label="Classify news content")


if submit:
    # classify news content by using the API URL provided

    if detect(news) == "sw":

        keys = {"news": news}
        prediction = r.get(
            "https://limitless-forest-00896.herokuapp.com/news-prediction/", params=keys
        )

        # collect and print the result
        results = prediction.json()
        category = results["prediction"]
        probability = results["Probability"]

        # Display results of the NLP task
        st.header("Results")

        st.write(
            "News category is {} with a probabiliy of {} ".format(category, probability)
        )
    else:

        st.write("The news content is not in swahili language.Pleae make sure the input is in swahili language")


    st.write("Developed with Love by Davis David")
