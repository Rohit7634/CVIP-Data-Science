#!/usr/bin/env python
# coding: utf-8

# # IMDB data 

# In[62]:


import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[63]:


data=pd.read_csv('imdb_top_1000.csv')


# In[ ]:


#Top 10 rows of dataset


# In[64]:


data.head(10)


# In[ ]:


#Last 10 rows of dataset


# In[65]:


data.tail(10)


# In[9]:


#Find Shape of our data Set


# In[66]:


data.shape


# In[67]:


print("Number of rows",data.shape[0])
print("Number of Columns",data.shape[1])


# In[12]:


#Get information About Our dataset


# In[68]:


data.info()


# In[15]:


#check missing value in Dataset


# In[16]:


print("Any missing value? ",data.isnull().values.any())


# In[69]:


data.isnull().sum()


# In[70]:


sns.heatmap(data.isnull())


# In[71]:


miss_per=data.isnull().sum()*100/len(data)


# In[ ]:


#how much percentage missing value present


# In[72]:


print(miss_per)


# In[23]:


#Drop all the missing value


# In[73]:


data.dropna(axis=0)


# In[25]:


#check duplicate data


# In[74]:


dup=data.duplicated().any()
print("Any duplicate value present in Dataset ",dup)


# In[29]:


data=data.drop_duplicates()
data


# In[ ]:





# In[30]:


#Get Overall Statistic about the DataFrame


# In[75]:


#onlu numerical field
data.describe()


# In[76]:


#all value 
data.describe(include='all')


# In[33]:


#Display Title of the Movie Having Rating>=8


# In[77]:


data.columns


# In[46]:


data[data['IMDB_Rating']>=8]


# In[49]:


#Highest Average Voting


# In[79]:


data.groupby('Released_Year')['No_of_Votes'].mean()


# In[80]:


#Sorting the value


# In[89]:


data.groupby('Released_Year')['No_of_Votes'].mean().sort_values(ascending=False)


# In[93]:


sns.barplot(x='Released_Year',y='No_of_Votes',data=data.head(10))
plt.title("Voted By year")
plt.xticks(rotation=90)
plt.show()


# In[ ]:


#Find The Vaerage Rating For Each Director


# In[97]:


data.groupby('Director')['IMDB_Rating'].mean().sort_values(ascending=False)


# In[101]:


sns.barplot(x='Director',y='IMDB_Rating',data=data.head(10))
plt.title("Rating Of the director movie")
plt.xticks(rotation=90)
plt.show()


# In[102]:


#Number of Movie Per Year


# In[113]:


p_y=data['Released_Year'].value_counts().sort_values(ascending=False)
print(p_y)


# In[117]:


sns.countplot(x='Released_Year',data=data)
plt.xticks(rotation=90)
plt.show()


# In[119]:


sns.barplot(x=p_y.index[0:10],y=p_y.values[0:10])
plt.title("Movie per years")
plt.xlabel("Years")
plt.ylabel("Number of Movies")
plt.show()


# In[124]:


rat=data['IMDB_Rating']
Gen=data['Genre']
r=rat.head(10)
g=Gen.head(10)


# In[141]:


plt.bar(r,g)
plt.xticks(rotation=90)


# In[140]:


plt.plot(rat[0:10],Gen[0:10])
plt.xticks(rotation=90)


# In[136]:


plt.barh(rat[0:10],Gen[0:10])
plt.xticks(rotation=90)


# In[134]:


sns.barplot(x=r,y=g)
plt.xticks(rotation=90)

