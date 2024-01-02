#!/usr/bin/env python
# coding: utf-8

# In[1]:


mylist = [1,2,3]


# In[3]:


myset = set()


# In[4]:


type(myset)


# In[5]:


type(mylist)


# In[44]:


class Dog():
    
    # CLASS OBJECT ATTRIBUTE
    # SAME FOR ANY INSTANCE OF THE CLASS
    species = 'mammal'
    
    def __init__(self,breed,name):
        
        #Attributes
        #We take in the argument
        #Assign it using self.attribute_name
        self.breed = breed
        self.name = name
        
    # OPERATIONS/Actions ---> Methods
    def bark(self,number):
        print("WOOF! My name is {} and the number is {}".format(self.name,number))


# In[45]:


my_dog = Dog('Labrador','Frankie')


# In[46]:


type(my_dog)


# In[47]:


my_dog.species


# In[48]:


my_dog.bark(10)


# In[ ]:





# In[ ]:





# In[61]:


class Circle():
    
    # CLASS OBJECT ATTRIBUTE
    pi = 3.14
    
    def __init__(self,radius=1):
        
        self.radius = radius
        self.area = radius*radius*Circle.pi
        
    # METHOD
    def get_circumference(self):
        return self.radius * Circle.pi * 2


# In[62]:


my_circle = Circle(30)


# In[63]:


my_circle.pi


# In[64]:


my_circle.radius


# In[65]:


my_circle.area


# In[66]:


my_circle.get_circumference()


# In[ ]:





# In[29]:


class Animal():
    
    def __init__(self,):
        print("ANIMAL CREATED")
        
    def who_am_i(self):
        print("I am an animal")
        
    def eat(self):
        print("I am eating")


# In[30]:


class Dog(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print("I am a dog and eating")
        
    def bark(self):
        print("WOOF!")


# In[31]:


mydog = Dog()


# In[32]:


mydog.eat()


# In[33]:


mydog.bark()


# In[20]:


mydog.who_am_i()


# In[4]:


myanimal = Animal()


# In[21]:


myanimal.eat()


# In[34]:


class Dog():
    
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        return self.name + "says woof!"


# In[35]:


class Cat():
    
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        return self.name + "says meow!"


# In[36]:


niko = Dog("niko")
felix = Cat("felix")


# In[37]:


print(niko.speak())


# In[39]:


print(felix.speak())


# In[44]:


for pet in [niko,felix]:
    
    print(type(pet))
    print(pet.speak())


# In[45]:


def pet_speak(pet):
    print(pet.speak())


# In[46]:


pet_speak(niko)


# In[47]:


pet_speak(felix)


# In[48]:


class Animal():
    
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")


# In[49]:


class Dog(Animal):
    
    def speak(self):
        return self.name + " says woof!"


# In[50]:


class Cat(Animal):
    
    def speak(self):
        return self.name + " says meow!"


# In[51]:


fido = Dog("Fido")


# In[52]:


isis = Cat("Isis")


# In[53]:


print(fido.speak())


# In[54]:


print(isis.speak())


# In[55]:


mylist = [1,2,3]


# In[56]:


len(mylist)


# In[57]:


class Sample():
    pass


# In[58]:


mysample = Sample()


# In[60]:


print(mysample)


# In[86]:


class Book():
    
    def __init__(self,title,author,pages):
        
        self.title = title
        self.author = author
        self.pages = pages
        
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print("A book object has been deleted")


# In[87]:


b = Book("Python rocks","Jose",200)


# In[88]:


print(b)


# In[89]:


str(b)


# In[90]:


len(b)


# In[91]:


del b


# In[8]:


class Person():
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def myfunc(self):
        print ("Hello, my name is " + self.name)
    
p1 = Person("John", 36)

p1.age = 50

print(p1.age)


# In[21]:


class Motorcycle():
    
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        
m1 = Motorcycle("Harley", "Sportster", 2002, "red")

print(m1.brand)
print(m1.model)
print(m1.color)
print(m1.year)


# In[39]:


class Account():
        
        def __init__(self, owner, balance):
            
            self.owner = owner
            self.balance = balance
            
        def __str__(self):
            return f"Account owner: {self.owner}\nAccount balance: {self.balance}"
        
        def deposit(self, amount):
            self.amount = amount
            print("Deposit accepted")
            self.balance += self.amount
            return self.balance
            
        def withdrawal(self, amount):
            self.amount = amount
            if self.amount > self.balance:
                return "Insufficient funds"
            else:
                print("Withdrawal accepted!")
                self.amount -= self.amount
                return self.balance
            
acct1 = Account("Stephen", 100)


# In[40]:


print(acct1)


# In[41]:


acct1.balance


# In[42]:


acct1.owner


# In[43]:


acct1.deposit(100)


# In[45]:


acct1.withdrawal(400)


# In[4]:


class Person():
    
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        
    def printname(self):
        print(self.firstname, self.lastname)
        
x = Person("Stephen", "Palmer")
x.printname()


# In[14]:


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = 2023
        
    def welcome(self):
         print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear) 

x = Student("Darren","Palmer", 2023)


# In[53]:


grade = int(input("Enter a grade: "))
if grade > 90:
    print("Student has earned an A")
elif grade > 80 and grade <= 90:
    print("Student has earned a B")
elif grade >= 60 and grade <= 80:
    print("Student has earned a C")
    
else:
    print("Student has earned a D")


# In[54]:


x = Student("Crystal","Parker")
x.printname()


# In[ ]:




