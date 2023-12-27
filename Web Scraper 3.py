#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Get the title of every book with a 2 star rating


# In[2]:


import requests


# In[3]:


import bs4


# In[4]:


'http://books.toscrape.com/catalogue/page-2.html'


# In[5]:


base_url = 'http://books.toscrape.com/catalogue/page-{}.html'


# In[6]:


page_num = 12
base_url.format(page_num)


# In[14]:


res = requests.get(base_url.format(1))


# In[15]:


soup = bs4.BeautifulSoup(res.text,'lxml')


# In[16]:


products = soup.select(".product_pod")


# In[17]:


example = products[0]


# In[26]:


example.select('a')[1]['title']


# In[27]:


two_star_titles = []

for n in range(1,51):
    
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)
    
    soup = bs4.BeautifulSoup(res.text,'lxml')
    books = soup.select(".product_pod")
    
    for book in books:
        # alternative option is if 'star-rating Two' in str(book)
        if len(book.select('.star-rating.Two')) != 0:
            book_title = book.select('a')[1]['title']
            two_star_titles.append(book_title)


# In[28]:


two_star_titles


# In[ ]:




