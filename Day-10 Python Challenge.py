#!/usr/bin/env python
# coding: utf-8

# # Day-10 Python Challenge

# # Creating a Dictionary 

# In[2]:


a = {
    "Id" :"1ab",
    "Age" :12,
    "Year" :2024,
    "Colour" :"Black"
}


# In[3]:


print(a)
print(type(a))


# In[4]:


a = {
    "Id" :"1ab",
    "Age" :12,
    "Year" :2024,
    "Colour" :"Black"
}


# In[5]:


print(a["Year"])


# # Access Function

# In[6]:


a = {
    "Id" :"1ab",
    "Age" :12,
    "Year" :2024,
    "Colour" :"Black",
    "Colour" :"Blue"
}


# In[8]:


print(a["Colour"]) ## Dictionary don't allow the duplicates


# # Length in dictionary 

# In[9]:


a = {
    "Id" :"1ab",
    "Age" :12,
    "Year" :2024,
    "Colour" :"Black"
}


# In[10]:


print(len(a))


# # Data types in dictionary

# In[11]:


a = {
    "Id" :"1ab", ## String Data type
    "Age" :12, ## Int Data Type
    "Year" :2024, ## Int Data Type
    "Colour" :"Black", ## String Data Type
    'b' :[1,2,3,4,5], ## List Data Type
    'c' :(2.3,2.4,2.5), ## Tuple Data Type
    'd' : True ## Boolean Data Type
}


# In[12]:


print(a)


# # Key Function

# In[15]:


a = {
    "Id" :"1ab",
    "Age" :12,
    "Year" :2024,
    "Colour" :"Black"
}
x = a.keys()
print(x)


# # Find Values Function

# In[16]:


a = {
    "Id" :"1ab",
    "Age" :12,
    "Year" :2024,
    "Colour" :"Black"
}
x = a.values()
print(x)


# # Change Function

# In[19]:


a = {
    "Id" :"1ab",
    "Age" :12,
    "Year" :2024,
    "Colour" :"Black"
}
a["Age"] = 19
print(a)


# # Update Function

# In[20]:


a = {
    "Id" :"1ab",
    "Age" :12,
    "Year" :2024,
    "Colour" :"Black"
}
a.update({"Mail Id" :"np897923@gmail.com"})
print(a)


# # Remove Function denoted by pop()

# In[21]:


a = {
    "Id" :"1ab",
    "Age" :12,
    "Year" :2024,
    "Colour" :"Black"
}
a.pop("Id")
print(a)


# # Clear Function

# In[22]:


a = {
    "Id" :"1ab",
    "Age" :12,
    "Year" :2024,
    "Colour" :"Black"}
a.clear()
print(a) ## They get the empty dictionary and to clear all the contant of the Dictionary.


# # Concatenate Function

# In[24]:


dict1 = {1:10, 2:20}
dict2 = {3:30, 4:40}
dict3 = {5:50, 6:60}
dict4 ={}
for d in (dict1, dict2, dict3): dict4.update(d)
print(dict4)

