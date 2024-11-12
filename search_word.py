#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('jupyter nbconvert --to script search_tools.ipynb')


# In[3]:


import mistune


# In[1]:


#Import Modules
import os
import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity


# In[3]:


#Load Database (pickle_file)
pickle_folder = os.path.join(".","pickle_file")


# In[4]:


#Load all pickle files and merge into single database
database = []
for pickle_file in os.listdir(pickle_folder):
    if pickle_file.endswith('.pkl'):
        with open(os.path.join(pickle_folder, pickle_file), "rb") as f:
            database.extend(pickle.load(f))


# In[5]:


#Simple Search
def simple_search(query, num_results=5):
    results = []
    query = query.lower()
    for entry in database:
        if query in entry['KEYWORD'].lower():
            results.append(entry)
    
    results = results[:num_results]
    
    for result in results:
        print(f"TEXT: {result['TEXT']}\nLINE: {result['LINE']}\nBOOK: {result['BOOK']}\nKEYWORD: {result['KEYWORD']}\n")
    
    return results


# In[6]:


#TF-IDF Search
def tfidf_search(query, num_results=5):
    documents = [entry['KEYWORD'] for entry in database]
    vectorizer = TfidfVectorizer(min_df=2)
    tfidf_matrix = vectorizer.fit_transform(documents)
    query_vec = vectorizer.transform([query.lower()])
    scores = cosine_similarity(query_vec, tfidf_matrix).flatten()
    top_indices = scores.argsort()[-num_results:][::-1]
    
    results = [database[i] for i in top_indices]
    for result in results:
        print(f"TEXT: {result['TEXT']}\nLINE: {result['LINE']}\nBOOK: {result['BOOK']}\nKEYWORD: {result['KEYWORD']}\n")
    
    return results, vectorizer, tfidf_matrix


# In[7]:


def svd_search(query, num_results=5):
    documents = [entry['KEYWORD'] for entry in database]
    vectorizer = TfidfVectorizer(min_df=2)
    tfidf_matrix = vectorizer.fit_transform(documents)
    svd = TruncatedSVD(n_components=100)
    svd_matrix = svd.fit_transform(tfidf_matrix)
    query_vec = svd.transform(vectorizer.transform([query.lower()]))
    scores = cosine_similarity(query_vec, svd_matrix).flatten()
    top_indices = scores.argsort()[-num_results:][::-1]
    top_terms = [vectorizer.get_feature_names_out()[idx] for idx in svd.components_.argsort()[::-1][:10]]
    
    results = [database[i] for i in top_indices]
    for result in results:
        print(f"TEXT: {result['TEXT']}\nLINE: {result['LINE']}\nBOOK: {result['BOOK']}\nKEYWORD: {result['KEYWORD']}\n")
    
    print("Top Keywords:\n")
    for terms in top_terms:
        print(terms)

    return results, top_terms


# In[8]:


#Testing
query = "shop"


# In[9]:


simple_search(query)


# In[10]:


tfidf_results, vectorizer, tfidf_matrix = tfidf_search(query)
print("TF-IDF Search:", tfidf_results)


# In[11]:


svd_results, top_terms = svd_search(query)


# In[ ]:




