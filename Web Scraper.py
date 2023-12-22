#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[2]:


import bs4


# In[3]:


result = requests.get("http://www.example.com")


# In[4]:


type(result)


# In[5]:


result.text


# In[6]:


soup = bs4.BeautifulSoup(result.text,"lxml")


# In[7]:


soup


# In[12]:


soup.select('title')[0].getText()


# In[13]:


site_paragraphs = soup.select("p")


# In[17]:


site_paragraphs[0].getText()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[18]:


res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')


# In[19]:


soup = bs4.BeautifulSoup(res.text,"lxml")


# In[20]:


soup


# In[25]:


first_item = soup.select('.vector-toc-link')[0]


# In[28]:


for item in soup.select('.vector-toc-link'):
    print(item.text)


# In[ ]:




