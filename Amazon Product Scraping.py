#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Load modules, open Chrome browser and webpage
import pandas as pd
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.get('https://www.amazon.in')


# In[2]:


#Get the Input Elements
input_search = driver.find_element(By.ID,"twotabsearchtextbox")


# In[3]:


search_button = driver.find_element(By.XPATH,"(//input[@type='submit'])[1]")


# In[4]:


#Send the Input to the Webpage
input_search.send_keys("Smartphones under 10000")
sleep(1)
search_button.click()


# In[5]:


product_class = 'a-size-medium a-color-base a-text-normal'


# In[8]:


#Scrape Products from Amazon
products = []
for i in range(10):
    print('Scraping page', i+1)
    product = driver.find_elements(By.XPATH,"//span[@class='a-size-medium a-color-base a-text-normal']")
    for p in product:
        products.append(p.text)
    next_button = driver.find_element(By.XPATH,"//a[@class='s-pagination-item s-pagination-next s-pagination-button s-pagination-separator']")
    next_button.click()
    sleep(4)


# In[ ]:


df = pd.DataFrame({'products': products})


# In[ ]:


df.to_csv('smartphone_data.csv', index=False)
print(df)


# In[ ]:




