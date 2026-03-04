# 🍔 McDonald Sentiment Analysis

McDonald Sentiment Analysis is a Natural Language Processing (NLP) sentiment analysis project that examines McDonald's customer feedback. The goal of this project is to identify sentiments as *positive*, *neutral*, or *negative* based on customer review data and provide insights into the model's performance. For deployment, I added a functionality to the review page that allows the model to respond to a customer's review with one of three possible answers: positive, neutral, or negative.

------------------------------------------------------------------------

## 📌 Background

In the current digital era, customers actively provide reviews of services and products thru various online platforms. McDonald's, as one of the largest F&B brands, has thousands of customer reviews containing opinions, criticisms, and suggestions.

Understanding those reviews manually is certainly not efficient. Therefore, this project was built to automate the sentiment analysis process using Machine Learning and NLP approaches so that the company can:

- Understanding customer perceptions quickly 
- Identifying potential service issues 
- Supporting data-driven decision-making

------------------------------------------------------------------------

## 🎯 Project Objective

The main objective of this project is:

- Developing an NLP-based sentiment classification model 
- Converting review texts into numerical representations using Sentence Transformers 
- Classifying sentiment using Support Vector Machine (SVM) 
- Evaluating model performance using precision, recall, F1-score, and accuracy 
- Providing visual insights from review data

------------------------------------------------------------------------

## 🛠️ Tech Stack

-   Python
-   Sentence Transformers
-   Scikit-learn
-   Support Vector Machine (SVM)
-   Pandas & NumPy
-   Matplotlib & Seaborn
-   Visual Studio Code

------------------------------------------------------------------------

## 📊 Dataset

The dataset used comes from Kaggle:

McDonald's Review Dataset 
https://www.kaggle.com/datasets/nelgiriyewithana/mcdonalds-store-reviews

This dataset contains thousands of customer reviews that are then processed and classified into three sentiment categories.

------------------------------------------------------------------------

## 🧠 Model Overview

This project uses a two-phase approach:

1. Sentence Transformers to generate sentence embeddings that can capture the context and meaning of sentences semantically. 
2. Support Vector Machine (SVM) as a classifier because it is effective on high-dimensional data and can form an optimal decision boundary.

The evaluation results show that the pre-tuning model was chosen because it has a more stable balance of precision and recall, thereby minimizing the potential for bias and excessive false positives.


------------------------------------------------------------------------

## 🗂️ Repository Structure

    📦 McDonald-Sentiment-Analysis
     ┣ 📂 data
     ┣ 📂 notebooks
     ┣ 📂 src
     ┣ 📂 images
     ┃ ┗ workflow.png
     ┣ README.md
     ┣ requirements.txt
     ┗ LICENSE

Explanation:

- `data/` → Raw dataset and preprocessing results 
- `notebooks/` → EDA, training, and model evaluation 
- `src/` → Modular scripts for preprocessing and modeling 
- `images/workflow.png` → Project process flow diagram 
- `requirements.txt` → Project dependencies

------------------------------------------------------------------------

## 🔄 Project Workflow

The complete project workflow can be found in the file:

images/workflow.png

The diagram explains the flow starting from data preprocessing, embedding generation, model training, to evaluation.

------------------------------------------------------------------------

## 🚀 How to Run

Clone repository:

``` bash
git clone https://github.com/ghozieikhsanf/McDonald-Sentiment-Analysis.git
```

Install dependencies:

``` bash
pip install -r requirements.txt
```

Run notebook to explore !!!

------------------------------------------------------------------------
## 🚀 Deployment

Check this out:
https://huggingface.co/spaces/ghozieikhsanf/McDonalds_Sentiment_Analysis

------------------------------------------------------------------------
## 👨‍💻 Author

Ghozie Ikhsan
Data Enthusiast | NLP & Machine Learning
