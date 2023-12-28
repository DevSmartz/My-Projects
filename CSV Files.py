#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv


# In[2]:


# Open the file
data = open('example.csv',encoding='utf-8')


# In[3]:


# csv.reader
csv_data = csv.reader(data)


# In[4]:


# reformat it into a Python object lists
data_lines = list(csv_data)


# In[5]:


data_lines[0]


# In[6]:


len(data_lines)


# In[7]:


for line in data_lines[:5]:
    print(line)


# In[8]:


data_lines[10][3]


# In[9]:


all_emails = []


# In[10]:


for line in data_lines[1:]:
    all_emails.append(line[3])


# In[11]:


all_emails


# In[12]:


# all_emails


# In[13]:


data_lines[10]


# In[14]:


full_names = []


# In[15]:


for line in data_lines[1:]:
    full_names.append(line[1]+' '+line[2])


# In[16]:


full_names


# In[17]:


file_to_output = open('to_save_file.csv','w',newline='')


# In[18]:


csv_writer = csv.writer(file_to_output,delimiter=',')


# In[19]:


csv_writer.writerow(['a','b','c'])


# In[20]:


csv_writer.writerows([['1','2','3'],['4','5','6']])


# In[21]:


file_to_output.close()


# In[22]:


f = open('to_save_file.csv',mode='a',newline='')


# In[23]:


csv_writer = csv.writer(f)

csv_writer.writerow(['new','new','new'])
# In[24]:


f.close()


# In[ ]:




