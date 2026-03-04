
import streamlit as st
import pandas as pd
import os
import pickle
from sentence_transformers import SentenceTransformer

# load all models dump
with open('/app/src/embedding_classification.pkl', 'rb') as file1:
    model_embed = pickle.load(file1)

embedder = SentenceTransformer('all-MiniLM-L6-v2')


def run():

    st.title("Welcome to McDonald's Customer Review!!")
    st.subheader("Review Form")
    with st.form("prediction_form"):
        review_form = st.text_input("REVIEW_FORM")
        submit = st.form_submit_button("Submit Your Review")


    data_inf = [review_form]
    st.dataframe(data_inf)

    if submit:
        new_embed = embedder.encode(data_inf, show_progress_bar=True)
        y_pred_inf = model_embed.predict(new_embed)
        if y_pred_inf == 'positive':
            st.write(f"Thank you for your review. McDonald's always served good experience. We're happy to see you returning soon!!!")
        elif y_pred_inf == 'neutral':
            st.write(f"Thank you for your review. McDonald's always improving time to time. We're happy to see you returning soon!!!")
        else :
            st.write(f"We're really sorry about your bad experience. Thank you for your review. McDonald's always improving time to time. We're happy to see you returning soon!!!")
            

if __name__ == '__main__':
    run()
