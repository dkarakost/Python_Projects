#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


weather = pd.read_csv("utrecht.csv" , index_col="datetime")


# In[5]:


weather


# In[9]:


weather.apply(pd.isnull).sum()/weather.shape[0]


# In[10]:


null_data = weather[["stations","preciptype"]].copy()


# In[11]:


null_data.columns = ["stations","preci"]


# In[12]:


null_data


# In[14]:


null_data["stations"].value_counts()


# In[24]:


#checking data types in null_data
null_data.dtypes


# In[25]:


#looking the index of null_data
null_data.index


# In[26]:


#
null_data.index = pd.to_datetime(null_data.index)


# In[32]:


#showing the max temparature and thin min for the whole timeline
weather[["tempmax", "tempmin"]].plot()


# In[36]:


#also for the humidity 
weather[["humidity"]].plot()


# ## Machine learing part

# In[39]:


weather["target"] = weather.shift(-1)["tempmax"]


# In[44]:


import sklearn as sl


# In[45]:


from sklearn.linear_model import Ridge


# In[47]:


rr = Ridge(alpha =.1)


# In[49]:


predictors = weather.columns[~weather.columns.isin(["name", "stations", "icon", "description", "target" , "condition"])]


# In[51]:


predictors


# In[64]:


grouped = weather.groupby(["datetime" , "icon"]).uvindex.count().reset_index()


# In[65]:


#grouped the data by daytime and icon and solarenergy
grouped


# In[ ]:




