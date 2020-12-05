#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import sys
import numpy as np


# In[23]:


df=pd.read_csv('data.csv', header=None, names=['Year', 'Export','Import','Trade Balance','Rate of Change Export %','Rate of Chnage import %'])

df=df.dropna(axis=0, how='any')
df=df.drop(0)


# In[24]:


df


# In[25]:


#plot scatter with first column as x values and second column as y values
plt.scatter(np.array(df['Export']).astype(np.float),np.array(df['Import']).astype(np.float),color='#dd12dd')

#specifying labels
plt.xlabel("export")
plt.ylabel("import")
plt.xticks(rotation='vertical')


# In[26]:


df=pd.read_csv('data.csv', header=None, names=['Year', 'Export','Import','Trade Balance','Rate of Change Export %',
                                                       'Rate of Chnage import %'])
for index in range(0,50):
      df = df.drop(index)


#plot bar plot with xticks which is position of bars as first argument and height of bars as second argument
plt.bar(range(1,16),np.array(df['Export']).astype(np.float),color='blue',label="export")

#specify labels on xticks
plt.xticks(range(1,16),df['Export'],rotation='vertical')
plt.xlabel("Years")
plt.ylabel("Export")


# In[27]:


df=pd.read_csv('data.csv', header=None, names=['Year', 'Export','Import','Trade Balance','Rate of Change Export %',
                                                       'Rate of Chnage import %'])
df = df.dropna(axis=0,how='any').drop(0)
plotMap=[]

#create a list of lists where each list will have a corresponding box plot
plotMap.append(np.array(df['Export']).astype(np.float).tolist())
plotMap.append(np.array(df['Import']).astype(np.float).tolist())

#plotting
plt.boxplot(plotMap)

#specifying labels
plt.xticks([1,2],["Exports","Imports"])
plt.ylabel("in Crores")


# In[ ]:




