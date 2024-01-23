#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
driver=webdriver.Chrome()
driver.get("https://www.instagram.com/")


# In[2]:


get_ipython().system('pip3 install wget')


# In[3]:


import os
import wget


# In[4]:


username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

username.clear()
password.clear()
username.send_keys("CzechMajestic2018x")
password.send_keys("LKGroE3QLx5")


# In[5]:


log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()


# In[10]:


not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[role='button']"))).click()


# In[11]:


not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()


# In[18]:


import time

#target the search input field
searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
searchbox.clear()

hashtag = "cat"
driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
time.sleep(5)


# In[20]:


driver.execute_script("window.scrollTo(0,4000);")


# In[23]:


images = driver.find_elements(By.TAG_NAME, 'img')


# In[25]:


images = [image.get_attribute('src') for image in images]


# In[30]:


images = images[:-2]


# In[31]:


print('Number of scraped images: ', len(images))


# In[32]:


images


# In[40]:


import pandas as pd


# In[41]:


df = pd.DataFrame({'images': images})


# In[42]:


df.to_csv('instagram_cats.json', index=False)
print(df)


# In[ ]:




