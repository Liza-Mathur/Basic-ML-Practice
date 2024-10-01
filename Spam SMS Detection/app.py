import streamlit as st
import pickle as pkl
import pickle as pkl
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
# from sklearn.feature_extraction.text import TfidfVectorizer

ps = PorterStemmer()
words = stopwords.words('english')

def text_transform(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum() and i not in words:
            y.append(ps.stem(i))

    return " ".join(y)

tfidf = pkl.load(open('vectorizer.pkl' , 'rb'))
vc = pkl.load(open('algorithm.pkl' , 'rb'))

st.title("SMS Classifier")

text = st.text_input("Enter the message")
if st.button('Predict'):
    text = text_transform(text)
    vect = tfidf.transform([text])
    print(text)
    res = vc.predict(vect)[0]
    print(res)

    if res == 1:
        st.header("Spam")
    else :
        st.header("Ham")