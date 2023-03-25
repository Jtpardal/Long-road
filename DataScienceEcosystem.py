#!/usr/bin/env python
# coding: utf-8

# # Data Science Tools and Ecosystem
# 
# 

# ***

# In this notebook, Data Science Tools and Ecosystem are summarized.

# --------------------------------------------------------------------------------------------------------------------------------

# **Objectives:**
#     -arithmetic expression
#     -convert minutes to hours
#     -Data Science tools
#     -libraries used by Data Scientists

# ***

# 1. Python
# 2. R
# 3. SQL
# 4. Java

# - Pandas
# - NumPy
# - Matplotlib

# 
# | Data Science Tool | 
# | -------------| 
# | Jupyter notebook | 
# | Jupyter Lab | 
# | Apache Zeppelin | 

# H3: Below are a few examples of evaluating arithmetic expressions in Python

# ***Below are a few examples of evaluating arithmetic expressions in Python

# ### H3: Below are a few examples of evaluating arithmetic expressions in Python

# ###: Below are a few examples of evaluating arithmetic expressions in Python

# ### Below are a few examples of evaluating arithmetic expressions in Python

# In[3]:


(3*4)+5 # This a simple arithmetic expression to mutiply then add integers


# In[2]:


time = int(input('number: '))
unit = input('(M)in or (H)ou: ')
if unit.upper() == "H":
    converted = time * 60
    print(f"You are {converted} Min")
else:
    converted = time / 60
    print(f"You are {converted} Hours")


# ## Author
# João Pardal

# In[ ]:




