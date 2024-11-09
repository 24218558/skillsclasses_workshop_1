#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import Modules
import os
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD


# In[2]:


#Load Database (pickle_file)
pickle_folder = ".\pickle_file"


# In[3]:


#Load all pickle files and merge into single database
database = []
for pickle_file in os.listdir(pickle_folder):
    if pickle_file.endswith('.pkl'):
        with open(os.path.join(pickle_folder, pickle_file), "rb") as f:
            database.extend(pickle.load(f))


# In[4]:


#Simple Search
def simple_search(query, num_results=5):
    results = []
    query = query.lower()
    for entry in database:
        if query in entry['Processed Text'].lower():
            results.append(entry)
    return results[:num_results]


# In[5]:


#TF-IDF Search
def tfidf_search(query, num_results=5):
    documents = [entry['Processed Text'] for entry in database]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)
    query_vec = vectorizer.transform([query.lower()])
    scores = (tfidf_matrix*query_vec.T).toarray().flatten()
    top_indices = scores.argsort()[-num_results:][::-1]
    return [database[i] for i in top_indices]


# In[6]:


def svd_search(query, num_results=5):
    documents = [entry['Processed Text'] for entry in database]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)
    svd = TruncatedSVD(n_components=100)
    svd_matrix = svd.fit_transform(tfidf_matrix)
    query_vec = svd.transform(vectorizer.transform([query.lower()]))
    scores = (svd_matrix @ query_vec.T).flatten()
    top_indices = scores.argsort()[-num_results:][::-1]
    return [database[i] for i in top_indices]


# In[7]:


#Testing


# In[8]:


query = "shop"
print("Simple Search:", simple_search(query))


# In[9]:


query = "shop"
print("TF-IDF Search:", tfidf_search(query))


# In[10]:


query = "shop"
print("SVD Search:", svd_search(query))


# In[ ]:




