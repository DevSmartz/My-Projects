#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests


# In[3]:


import bs4


# In[4]:


res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")


# In[5]:


soup = bs4.BeautifulSoup(res.text,"lxml")


# In[6]:


soup


# In[17]:


soup.select('img')[4]


# In[19]:


computer = soup.select('img')[4]


# In[21]:


computer['src']


# <img
# src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg">

# In[22]:


image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg')


# In[23]:


image_link.content


# In[24]:


f = open('my_computer_image.jpg','wb')


# In[25]:


f.write(image_link.content)


# In[26]:


f.close()


# In[ ]:




