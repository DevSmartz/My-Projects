#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pd

from selenium.webdriver.common.by import By

from selenium import webdriver

driver=webdriver.Chrome()

driver.get("https://www.superyachttimes.com/yachts")


# In[2]:


Json_tag = driver.find_element(By.ID,"__NEXT_DATA__")


# In[3]:


Json_tag.text


# In[4]:


from bs4 import BeautifulSoup


# In[5]:


Soup = BeautifulSoup(driver.page_source, 'html.parser')


# In[6]:


Soup.contents


# In[7]:


import json


# In[8]:


data = json.loads(Soup.find('script', {'id':'__NEXT_DATA__'}).text)


# In[9]:


data


# In[10]:


data.keys()


# In[11]:


data['props'].keys()


# In[12]:


data['props']['pageProps'].keys()


# In[13]:


data['props']['pageProps']['yachts']


# In[14]:


links = [item['link'] for item in data['props']['pageProps']['yachts']]


# In[15]:


links


# In[16]:


links = ['https://www.superyachttimes.com/yachts'+item['link'] for item in data['props']['pageProps']['yachts']]


# In[17]:


links


# In[18]:


links = ['https://www.superyachttimes.com/'+item['link'] for item in data['props']['pageProps']['yachts']]


# In[19]:


links


# In[20]:


links = ['https://www.superyachttimes.com'+item['link'] for item in data['props']['pageProps']['yachts']]


# In[21]:


links


# In[25]:


df = pd.DataFrame({'data': data})


# In[26]:


df.to_csv('yacht_data.csv', index=False)
print(df)


# In[ ]:




