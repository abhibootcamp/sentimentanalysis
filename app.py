import streamlit as st
from textblob import TextBlob
import matplotlib.pyplot as plt

# Streamlit UI
st.title("Sentiment Analysis")

# Text input
text = st.text_input("Enter text to analyze sentiment:")

if text:
    # Perform sentiment analysis
    blob = TextBlob(text)
    sentiment = blob.sentiment

    # Display sentiment result
    st.subheader("Sentiment Analysis Result:")
    st.write(f"Sentiment: {'Positive' if sentiment.polarity > 0 else 'Negative' if sentiment.polarity < 0 else 'Neutral'}")
    st.write(f"Confidence: {abs(sentiment.polarity):.2f}")

    # Visualization
    labels = ['Positive', 'Neutral', 'Negative']
    sizes = [sentiment.polarity + 1, 1, abs(sentiment.polarity) + 1]
    colors = ['#00ff00', '#cccccc', '#ff0000']
    explode = (0.1, 0, 0)  # explode 1st slice
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    st.subheader("Sentiment Distribution:")
    st.pyplot(plt)
