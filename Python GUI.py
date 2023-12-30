#!/usr/bin/env python
# coding: utf-8

# In[1]:


from ipywidgets import interact,interactive,fixed
import ipywidgets as widgets


# In[7]:


def func(x):
    return x


# In[9]:


interact(func,x='Hello')


# In[15]:


@interact(x=True,y=fixed(1.0))
def g(x,y):
    return (x,y)


# In[16]:


interact(func,x=widgets.IntSlider(min=-100,max=100,step=1,value=0))


# In[18]:


interact(func,x=(-10,10,1))


# In[19]:


@interact(x=(0.0,20.0,0.5))
def h(x=5.0):
    return x


# In[21]:


interact(func,x=['hello','option 2','option 3'])


# In[22]:


interact(func,x={'one':10,'two':20})


# In[24]:


from IPython.display import display

def f(a,b):
    display(a+b)
    return a+b


# In[25]:


w = interactive(f,a=30,b=40)


# In[26]:


type(w)


# In[27]:


w.children


# In[28]:


display(w)


# In[ ]:




