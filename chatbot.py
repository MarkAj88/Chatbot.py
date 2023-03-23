#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install nltk streamlit')

import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
import streamlit as st

import nltk
nltk.download('stopwords')

import nltk
nltk.download('wordnet')

# Load the text file and preprocess the data
with open('chatbot.txt', 'r', encoding='utf-8') as f:
    data = f.read().replace('\n', ' ')
# Tokenize the text into sentences
sentences = sent_tokenize(data)
# Define a function to preprocess each sentence
def preprocess(sentence):
    # Tokenize the sentence into words
    words = word_tokenize(sentence)
    # Remove stopwords and punctuation
    words = [word.lower() for word in words if word.lower() not in stopwords.words('french') and word not in string.punctuation]
    # Lemmatize the words
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    return words
# Preprocess each sentence in the text
corpus = [preprocess(sentence) for sentence in sentences]

def get_most_relevant_sentence(query):
    # Preprocess the query
    query = preprocess(query)
    
    # Initialize variables to store the most relevant sentence and its similarity score
    max_similarity = 0
    most_relevant_sentence = ""
    
    # Iterate over each sentence in the corpus
    for sentence in corpus:
        # Preprocess the sentence
        sentence = preprocess(sentence)
        
        # Compute the Jaccard similarity coefficient between the query and the sentence
        similarity = len(set(query).intersection(sentence)) / float(len(set(query).union(sentence)))
        
        # Update the most relevant sentence if the current sentence has a higher similarity score
        if similarity > max_similarity:
            max_similarity = similarity
            most_relevant_sentence = " ".join(sentence)
    
    # Return the most relevant sentence
    return most_relevant_sentence

def chatbot(question):
    # Find the most relevant sentence
    most_relevant_sentence = get_most_relevant_sentence(question)
    # Return the answer
    return most_relevant_sentence

def main():
    st.title("Chatbot")
    st.write("Hello! I'm a chatbot. Ask me anything about the topic in the text file.")
    # Get the user's question
    question = st.text_input("You:")
    # Create a button to submit the question
    if st.button("Submit"):
        # Call the chatbot function with the question and display the response
        response = chatbot(question)
        st.write("Chatbot: " + response)
if __name__ == "__main__":
    main()


# In[ ]:




