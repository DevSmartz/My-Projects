#!/usr/bin/env python
# coding: utf-8

# In[37]:


import requests


# In[38]:


import bs4


# In[39]:


res = requests.get("http://quotes.toscrape.com/")


# In[40]:


soup = bs4.BeautifulSoup(res.text,"lxml")


# In[51]:


soup


# In[64]:


text = soup.select('.text')


# In[65]:


text


# In[62]:


auth_list = soup.select('.author')


# In[63]:


auth_list


# In[68]:


authors = set([author.text for author in auth_list])


# In[69]:


authors


# In[66]:


auth_quotes = soup.select('.quote')


# In[67]:


auth_quotes


# In[74]:


quote_list = soup.select('.text')
quotations = [quote.text for quote in auth_quotes]


# In[100]:


quotations = ['“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”\nby Albert Einstein\n(about)\n\n\n            Tags:\n            \nchange\ndeep-thoughts\nthinking\nworld',
 '“It is our choices, Harry, that show what we truly are, far more than our abilities.”\nby J.K. Rowling\n(about)\n\n\n            Tags:\n            \nabilities\nchoices',
 '“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”\nby Albert Einstein\n(about)\n\n\n            Tags:\n            \ninspirational\nlife\nlive\nmiracle\nmiracles',
 '“The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”\nby Jane Austen\n(about)\n\n\n            Tags:\n            \naliteracy\nbooks\nclassic\nhumor',
 "“Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”\nby Marilyn Monroe\n(about)\n\n\n            Tags:\n            \nbe-yourself\ninspirational",
 '“Try not to become a man of success. Rather become a man of value.”\nby Albert Einstein\n(about)\n\n\n            Tags:\n            \nadulthood\nsuccess\nvalue',
 '“It is better to be hated for what you are than to be loved for what you are not.”\nby André Gide\n(about)\n\n\n            Tags:\n            \nlife\nlove',
 "“I have not failed. I've just found 10,000 ways that won't work.”\nby Thomas A. Edison\n(about)\n\n\n            Tags:\n            \nedison\nfailure\ninspirational\nparaphrased",
 "“A woman is like a tea bag; you never know how strong it is until it's in hot water.”\nby Eleanor Roosevelt\n(about)\n\n\n            Tags:\n            \nmisattributed-eleanor-roosevelt",
 '“A day without sunshine is like, you know, night.”\nby Steve Martin\n(about)\n\n\n            Tags:\n            \nhumor\nobvious\nsimile']
quotations = [r.replace("\n", "") for r in quotations]
print(quotations)


# In[76]:


top_ten_tags = soup.select('.tag-item')


# In[77]:


top_ten_tags


# In[88]:


tags = [tag.text for tag in top_ten_tags]


# In[91]:


tags


# In[92]:


tags = [r.strip() for r in tags]
print(tags)


# In[102]:


base_url = 'http://quotes.toscrape.com/page/{}/'


# In[104]:


page_num = 2
base_url.format(page_num)


# In[105]:


res = requests.get(base_url.format(1))


# In[106]:


soup = bs4.BeautifulSoup(res.text,'lxml')


# In[107]:


author = soup.select(".author")


# In[108]:


example = author[0]


# In[116]:


auth_list = []
author = []
base_url = "http://quotes.toscrape.com/page/{}/"


n = 0

while True: 
    n+= 1
    for page in range(n):
        res = requests.get(base_url.format(n))
        soup = bs4.BeautifulSoup(res.text, 'lxml')
        auth_list.append(soup.select('.author'))

    for i in auth_list:
        for j in i:
            author.append(j.text)
            
    if soup.select('.next') == []:
        break

author = set(author)
author


# In[ ]:




