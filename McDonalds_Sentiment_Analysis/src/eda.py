
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import re
from matplotlib.patches import Patch


st.set_page_config(
    page_title=" Welcome to McDonald's Reviews Analysis ",
    layout='wide',
    initial_sidebar_state='expanded'
)

def run():
    # membuat title
    st.title("McDonald's Reviews Analysis")

    # membuat subheader
    st.subheader('EXPLANATORY DATA ANALYSIS')

    # menambahkan gambar
    st.image('https://tse1.mm.bing.net/th/id/OIP.RmZj4-K5zb4pxdTgch6ptwHaHP?pid=Api&P=0&h=180',
            caption='https://tse1.mm.bing.net/th/id/OIP.RmZj4-K5zb4pxdTgch6ptwHaHP?pid=Api&P=0&h=180')
    
    # menambahkan deskripsi
    st.write('Created by Ghozie Ikhsan Fairuz')
    st.write('# EDA')
    st.write('## Simple Exploratory Data')
    st.write("### McDonald's Customer Reviews and Rating")

    # menggunakan sintaks markdown untuk buat garis lurus
    st.markdown('---')

    # Show dataframe
    df = pd.read_csv("/app/src/McDonald_s_Reviews.csv", encoding="latin1")
    st.dataframe(df)
    

    def clean_text(text):
        text = str(text).lower()
        text = re.sub(r"[^a-zA-Z\s\.]", "", text)  # keep huruf & titik
        text = re.sub(r"\s+", " ", text).strip()
        return text

    df["clean_text"] = df["review"].apply(clean_text)
    
    category_dict = {
        "food": ["food", "coffee", "taste", "meal"],
        "service": ["service", "staff", "waiter"],
        "price": ["price", "cost"]
    }

    expression_words = [
        "good", "bad", "terrible", "excellent",
        "slow", "friendly", "rude",
        "expensive", "cheap", "affordable",
        "worth", "overpriced"
    ]
    def extract_category_expression(df):

        results = []

        for rating in sorted(df["rating"].unique()):
            subset = df[df["rating"] == rating]["clean_text"]

            for text in subset:
                words = text.split()

                for i, word in enumerate(words):
                    for category, cat_words in category_dict.items():
                        if word in cat_words:
                            window = words[max(i-3,0): i+4]
                            for w in window:
                                if w in expression_words:
                                    results.append({
                                    "rating": rating,
                                    "category": category,
                                    "expression": w
                                })

        return pd.DataFrame(results)
    
    result_df = extract_category_expression(df)
    
    summary = (
        result_df
        .groupby(["rating", "category", "expression"])
        .size()
        .reset_index(name="count")
    )
    present_summary=summary.sort_values(['rating', 'count'], ascending=[True, False]) \
            .groupby('rating') \
            .head(3)
    st.set_page_config(layout="wide")

    st.title("Review Expression Analysis")
    # extract all expression value and sort
    all_expressions = sorted(present_summary["expression"].unique())

    # color palette adjusting
    palette = sns.color_palette("tab20", len(all_expressions))

    # mapping color palette with expression
    color_mapping = dict(zip(all_expressions, palette))


    # FacetGrid based on Rating
    g = sns.FacetGrid(
        present_summary,
        col="rating",      
        col_wrap=3,        
        sharex=False,      
        height=4           
    )

    # bcreat bar plot
    g.map_dataframe(
        sns.barplot,
        y="category",              
        x="count",                 
        hue="expression",          
        hue_order=all_expressions, 
        palette=color_mapping      
    )


    g.set_titles("{col_name}")
    g.set_axis_labels("Count", "Category")

    # delete default legend
    if g._legend:
        g._legend.remove()


    # create manual legend
    legend_elements = [
        Patch(facecolor=color_mapping[exp], label=exp)
        for exp in all_expressions
    ]

    g.fig.legend(
        handles=legend_elements,
        title="Expression",
        loc="center",
        bbox_to_anchor=(0.82, 0.25),
        frameon=True
    )

    plt.tight_layout()
    plt.show()
    st.pyplot(g.fig)
    
    st.subheader("Rating Distribution")
    rating_counts = df["rating"].value_counts().sort_index()

    rating_percent = rating_counts / rating_counts.sum() * 100
    fig, ax = plt.subplots()
    ax.pie(
        rating_percent,
        labels=rating_percent.index,
        autopct="%1.1f%%"
        )

    ax.set_title("Rating Distribution (1–5)")

    st.pyplot(fig)
    
    df['review_len'] = df['clean_text'].fillna('').str.len()
    
    stats = {
        'min_length': df['review_len'].min(),
        'max_length': df['review_len'].max(),
        'median_length': df['review_len'].median(),
        'mean_length': df['review_len'].mean()
    }

    st.subheader("📊 Review Length Statistics")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Min Length", int(stats['min_length']))
    col2.metric("Max Length", int(stats['max_length']))
    col3.metric("Median Length", int(stats['median_length']))
    col4.metric("Mean Length", round(stats['mean_length'], 2))
if __name__ == '__main__':
    run()
