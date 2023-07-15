#!/usr/bin/env python
# coding: utf-8

# In[82]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[83]:


data=pd.read_csv('data.csv')


# In[84]:


data.head()


# In[85]:


data


# In[86]:


data.info()


# In[87]:


data.dropna(inplace=True)


# In[88]:


data.info()


# In[89]:


from sklearn.model_selection import train_test_split

x=data.drop(['price'],axis=1)
y=data['price']


# In[20]:


y


# In[90]:


x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.2)


# In[91]:


train_data=x_train.join(y_train)


# In[92]:


train_data


# In[93]:


train_data.hist(figsize=(15,9))


# In[94]:


train_data.corr()


# In[95]:


sns.heatmap(train_data.corr())


# In[96]:


plt.figure(figsize=(15,8))
sns.heatmap(train_data.corr(),annot=True,cmap="YlGnBu")


# In[97]:


train_data["bedrooms"]=np.log(train_data["bedrooms"]+1)
train_data["sqft_living"]=np.log(train_data["sqft_living"]+1)
train_data["floors"]=np.log(train_data["floors"]+1)
train_data["sqft_lot"]=np.log(train_data["sqft_lot"]+1)


# In[98]:


train_data.hist(figsize=(15,8))


# In[99]:


train_data.view.value_counts()


# In[100]:


train_data=train_data.join(pd.get_dummies(train_data.view)).drop(['view'],axis=1)


# In[101]:


train_data


# In[102]:


plt.figure(figsize=(15,8))
sns.heatmap(train_data.corr(),annot=True,cmap="YlGnBu")


# In[105]:


plt.figure(figsize=(15,8))
sns.scatterplot(x='sqft_lot',y='sqft_living',data=train_data,hue="sqft_lot",palette="coolwarm")


# In[110]:


train_data['bedroom_ration']=train_data['bedrooms']/train_data['sqft_living']
train_data['household_ration']=train_data['sqft_lot']/train_data['sqft_living']


# In[114]:


plt.figure(figsize=(15,8))
sns.heatmap(train_data.corr(),annot=True,cmap="YlGnBu")


# In[115]:


train_data.info()


# In[135]:


from sklearn.linear_model import LinearRegression


x_train, y_train=train_data.drop(['price'],axis=1), train_data['price']



# In[ ]:





# In[136]:


train_data.info()


# In[125]:


reg=LinearRegression()
reg.fit(x_train,y_train)

