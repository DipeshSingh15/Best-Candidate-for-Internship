#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns


# In[2]:


df=pd.read_csv("C:\\Users\\Dipesh Singh\\Downloads\\Applications_for_Machine_Learning_internship_edited.xlsx - Sheet1.csv")


# In[11]:


df.head()


# # All columns name

# In[35]:


df.columns


# # Shape of dataset
# 

# In[13]:


df.shape


# # Filteration of available candidate

# In[7]:


df['Are you available for 3 months, starting immediately, for a full-time work from home internship? '].unique()


# In[24]:


df.iloc[:,6][0][0]


# In[28]:


df['Are you available for 3 months, starting immediately, for a full-time work from home internship? ']=df['Are you available for 3 months, starting immediately, for a full-time work from home internship? '].replace(['Yes, I am available for 3 months starting immediately for a full-time internship.'],1)
        
df['Are you available for 3 months, starting immediately, for a full-time work from home internship? '].unique()


# In[29]:


df.drop(df[df['Are you available for 3 months, starting immediately, for a full-time work from home internship? ']!=1].index,inplace=True)


# Size of data set after filteration

# In[30]:


df.shape     


# In[31]:


df['Are you available for 3 months, starting immediately, for a full-time work from home internship? '].unique()


# # Adding new feature named as skill score by adding skill values

# In[32]:


df["Skill Score"]=df['Python (out of 3)']+ df['Machine Learning (out of 3)']+ df['Natural Language Processing (NLP) (out of 3)']+df['Deep Learning (out of 3)']


# In[33]:


df.head()


# In[42]:


result=df.sort_values(["Skill Score"],ascending=False)


# In[43]:


result


# # After sorting the dataset now we can select the candidate for intership on the basis of their skill score.

# In[44]:


result.head(20)


# # Filled all null values

# In[45]:


df["Performance_PG"].fillna("0", inplace =True)


# In[46]:


df["Performance_UG"].fillna("0", inplace=True)


# In[47]:


df["Performance_12"].fillna("0", inplace=True)
df["Performance_10"].fillna("0", inplace=True)


# In[48]:


df.head()


# In[ ]:




