#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
import os


# In[2]:


sys.path.append(os.getcwd())


# In[3]:


# Import necessary libraries
from search_word import simple_search, tfidf_search, svd_search


# In[4]:


# Execute search with user input
def search_database(query, method='simple', num_results=5):
    if method == 'simple':
        return simple_search(query, num_results)
    elif method == 'tfidf':
        return tfidf_search(query, num_results)
    elif method == 'svd':
        return svd_search(query, num_results)
    else:
        print("Invalid search method.")
        return []


# In[7]:


#Testing
query = input("Enter your search query: ")
method = input("Enter search method (simple, tfidf, svd): ")
num_results = int(input("Enter number of results: "))
results = search_database(query, method, num_results)
for result in results:
    print(f"BOOK: {result['BOOK']}, LINE: {result['LINE']}\nTEXT: {result['TEXT']}\nKEYWORD: {result['KEYWORD']}\n")


# In[ ]:




