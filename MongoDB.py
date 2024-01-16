#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pymongo
import pandas as pd
import json


# In[3]:


client = pymongo.MongoClient("mongodb://localhost:27017")


# In[4]:


df = pd.read_csv("output5.csv") 


# In[5]:


df.head()


# In[6]:


df.tail()


# In[8]:


df.shape


# In[9]:


data = df.to_dict(orient = "records")


# In[10]:


data


# In[11]:


db = client["ScrapeData"]


# In[12]:


print(db)


# In[13]:


db.Scrape.insert_many(data)


# In[ ]:




