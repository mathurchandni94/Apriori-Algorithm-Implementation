#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[62]:


from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules


# In[78]:


transaction_data = pd.read_excel("C:/Users/Owner/Desktop/New folder (5)/Apriori Practice/Apriori_Practice_Data.xlsx")


# In[79]:


transaction_data.head()


# In[80]:


a=apriori(transaction_data,min_support=0.22)


# In[81]:


a


# In[84]:


rules=association_rules(a,metric='lift', min_threshold=1)
rules


# In[ ]:




