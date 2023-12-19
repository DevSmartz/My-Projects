#!/usr/bin/env python
# coding: utf-8

# In[1]:


def max_num(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3


# In[4]:


max_num(11,9,7)


# In[7]:


name = input("Please enter your name: ")


# In[1]:


ans_1 = input("Please enter your name.")

print("Hello!, " + ans_1)


# In[3]:


ans_1=input("Please enter your age. ")

print(type(ans_1))


# In[4]:


ans_1=int(input("Enter current year. " ))

print(ans_1 + 50)


# In[6]:


message=input("Please enter the number of miles.")

result=int(message)*1.609344


print(result)


# In[2]:


def sum(numbers):
    total = 0
    
    for x in numbers:
        total = total+x
        
    return total

print(sum((8, 2, 3, 0, 7))) 


# In[5]:


def multi(numbers):
    
    total = 1
    
    for i in numbers:
        total = total*i
        
    return total

print(multi((8, 2, 3, -1, 7)))


# In[1]:


def my_function(child3, child2, child1):
  print("The youngest child is " + child3) 


# In[2]:


my_function("Emil","Tobias","Linus")


# In[1]:


def evens(i):
    if i % 2 == 0:
        print(bool(True))
    else:
         print(bool(False))


# In[2]:


evens(98)


# In[11]:


treepersqkm = {"Finland": 90652, "Taiwan": 69593, "Japan": 49894, "Russia": 41396, "Brazil": 39542, "Canada": 36388, "Bulgaria": 24987, "France": 24436, "Greece": 24323, "United States": 23513, "Turkey": 11126, "India": 11109, "Denmark": 6129, "Syria": 534, "Saudi Arabia": 1}

def moretrees(dict):
    lst = []
    for i in dict:
        if dict[i]>20000:
            lst.append(i)
        else:
            pass
    return lst


# In[12]:


print(moretrees(treepersqkm))


# In[13]:


def vote(age):
    if age >= 18:
        print("You are eligible to vote")
    else:
        print("You are not eligible to vote")


# In[15]:


vote(41)


# In[19]:


num = int(input("Enter a number: "))
if num % 2 == 0:
    print("This number is even")
else:
    print("This number is odd")    


# In[21]:


number = int(input("Enter a number: "))
if number % 7 == 0:
    print("Number is divisible by 7")
else:
    print("Number is not divisible by 7")


# In[31]:


num = int(input("Enter a number: "))
if num % 5 == 0:
    print("Hello")
else:
    print("Bye")


# In[34]:


def reverse_words(text):
    words = text.split(" ")
    
    newwords = [word[::-1] for word in words]
    newText = " ".join(newwords)
    
    return newText    


# In[35]:


reverse_words('The quick brown fox jumps over the lazy dog.')


# In[7]:


city = input("Enter a city from India: ")
if city == "Delhi":
    print("The monument is Red Fort")
elif city == "Agra":
    print("The monument is Taj Mahal")
elif city == "jaipur":
    print("The monument is Jal Mahal")
else:
    print("This city is not valid!")


# In[ ]:


age = int(input("Enter your age: "))
if age >= 65:
    print("You are a senior citizen")
else:
    print("You are not a senior citizen")


# In[1]:


def lowest_num(num1, num2):
    if num1 > num2:
        return num1
    elif num1 < num2:
        return num2
    else:
        return("number not valid")


# In[ ]:




