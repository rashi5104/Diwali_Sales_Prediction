#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df=pd.read_csv(r'C:\\Users\\rashi\\Dropbox\\PC\\Desktop\\Diwali Sales Data.csv', encoding='latin1')
df


# In[3]:


df.shape


# In[4]:


df.head()


# In[5]:


df.tail()


# In[6]:


df.info()


# In[7]:


pd.isnull(df)


# In[8]:


df.drop(['Status','unnamed1'],axis=1,inplace=True)


# In[9]:


df.info()


# In[10]:


df.dropna(inplace=True)


# In[11]:


df


# In[12]:


# change data type
df['Amount']=df['Amount'].astype('int')


# In[13]:


df['Amount'].dtypes


# In[14]:


df.info()


# In[15]:


df.columns


# In[16]:


#rename column
df.rename(columns={'Marital_Status':'Shaadi'})


# In[17]:


#describe() method returns description of the data in the dataset(i.e.count,mean,std etc)
df.describe()


# In[18]:


# use describe() for specific columns
df[['Age','Orders','Amount']].describe()


# #  Exploratory Data Analysis

# # Gender

# In[19]:


df.columns


# In[20]:


sns.countplot(x='Gender',data=df)


# In[21]:


ax=sns.countplot(x='Gender',data=df)
for bars in ax.containers:
    ax.bar_label(bars)


# In[22]:


df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)


# In[23]:


sales_gen=df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.barplot(x='Gender',y='Amount',data=sales_gen)


# # From above graphs we can see that most of the buyers are females and even the purchasing power of females are greater than men

# # Age

# 

# In[24]:


df.columns


# In[25]:


sns.countplot(x='Age Group',data=df)


# In[26]:


sns.countplot(x='Age Group',hue='Gender',data=df)


# In[27]:


ax=sns.countplot(x='Age Group',hue='Gender',data=df)
for bars in ax.containers:
    ax.bar_label(bars)


# In[28]:


sales_age=df.groupby(['Age Group'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.barplot(x='Age Group',y='Amount',data=sales_age)


# # From above graph we can see that most of the buyers of age group between 26-35 years females

# # State

# In[29]:


df.columns


# In[30]:


sales_state=df.groupby(['State'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False)
sns.set(rc={'figure.figsize':(28,5)})
sns.barplot(x='State',y='Orders',data=sales_state)


# In[31]:


sales_state=df.groupby(['State'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.set(rc={'figure.figsize':(28,5)})
sns.barplot(x='State',y='Amount',data=sales_state)


# # From above graph we can see that most of the orders and total amount are from uttar pradesh,maharashtra and karnataka

# # Marital Status

# In[32]:


df.columns


# In[33]:


sns.countplot(x='Marital_Status',data=df)
sns.set(rc={'figure.figsize':(10,5)})


# In[34]:


ax=sns.countplot(x='Marital_Status',data=df)
sns.set(rc={'figure.figsize':(10,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[35]:


sales_state=df.groupby(['Marital_Status','Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.set(rc={'figure.figsize':(10,7)})
sns.barplot(x='Marital_Status',y='Amount',data=sales_state,hue='Gender')


# # From above graph we can see that most of the buyers are married(woman) and they have high purchasing power

# # Occupation 

# In[36]:


df.columns


# In[37]:


sns.set(rc={'figure.figsize':(20,10)})
sns.countplot(x='Occupation',data=df)


# In[38]:


sns.set(rc={'figure.figsize':(20,10)})
ax=sns.countplot(x='Occupation',data=df)
for bars in ax.containers:
    ax.bar_label(bars)


# In[39]:


sales_state=df.groupby(['Occupation'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.set(rc={'figure.figsize':(20,10)})
sns.barplot(data=sales_state,x='Occupation',y='Amount')


# # From above graph we can see that most of the buyers are working in IT sector,Healthcare and Aviation 

# # Product category

# In[40]:


df.columns


# In[41]:


sns.countplot(data=df,x='Product_Category')
sns.set(rc={'figure.figsize':(20,10)})


# In[42]:


sns.set(rc={'figure.figsize':(20,10)})
ax=sns.countplot(data=df,x='Product_Category')
for bars in ax.containers:
    ax.bar_label(bars)


# In[43]:


sales_state=df.groupby(['Product_Category'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)
sns.set(rc={'figure.figsize':(20,10)})
sns.barplot(x='Product_Category',y='Amount',data=sales_state)


# # From above graph we can see that most of the sold products are Food,Clothing and Electronic category

# # Product_ID

# In[44]:


df.columns


# In[45]:


sales_state=df.groupby(['Product_ID'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)
sns.set(rc={'figure.figsize':(20,10)})
sns.barplot(x='Product_ID',y='Orders',data=sales_state)


# # Conclusion

# #  Married woman age group 26-35 year from UP,Maharashtra,Karnataka working in IT, Healthcare and Aviation are more liked buy products from Food,Clothing and Electronic category

# # Zone

# In[46]:


sns.countplot(x='Zone',data=df)


# In[47]:


ax=sns.countplot(x='Zone',data=df)
for bars in ax.containers:
    ax.bar_label(bars)


# In[48]:


sales_state=df.groupby(['Zone'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.set(rc={'figure.figsize':(20,10)})
sns.barplot(x='Zone',y='Amount',data=sales_state)


# In[49]:


sales_state=df.groupby(['Zone'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False)
sns.set(rc={'figure.figsize':(20,10)})
sns.barplot(x='Zone',y='Orders',data=sales_state)


# In[ ]:





# In[ ]:




