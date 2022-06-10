#!/usr/bin/env python
# coding: utf-8

# Installing Libraries
# #First, please run this cell and restart your kernel.
# #These are all the libraries you need for this python notebook.
# 
# 
# 
# 

# In[ ]:


get_ipython().run_line_magic('pip', 'install pandas')
get_ipython().run_line_magic('pip', 'install numpy')
get_ipython().run_line_magic('pip', 'install scipy')
get_ipython().run_line_magic('pip', 'install seaborn')
get_ipython().run_line_magic('pip', 'install matplotlib')
get_ipython().run_line_magic('pip', 'install sklearn')
get_ipython().run_line_magic('pip', 'install plotly')

get_ipython().run_line_magic('pip', 'install --upgrade pandas')
get_ipython().run_line_magic('pip', 'install --upgrade numpy')
get_ipython().run_line_magic('pip', 'install --upgrade scipy')
get_ipython().run_line_magic('pip', 'install --upgrade seaborn')
get_ipython().run_line_magic('pip', 'install --upgrade matplotlib')
get_ipython().run_line_magic('pip', 'install --upgrade sklearn')
get_ipython().run_line_magic('pip', 'install --upgrade plotly')


# #importing libraries
# 

# In[3]:


#importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from scipy.stats import normaltest
from scipy import stats


#Libraries for model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler


# In[28]:


#this function is to read, transform and join 2 data frame
#%%
def read_secom():
    path = 'Downloads/secom.data'
    df = pd.read_csv(path, delimiter=' ', header=None, na_values=['NaN'])
    df.columns = ['feature'+str(x+1) for x in range(len(df.columns))]
    return df


#%%
def read_labels():
    path = 'Downloads/secom_labels.data'
    df = pd.read_csv(path, delimiter=' ', header=None, na_values=['NaN'])
    df.columns = ['status','timestamp']
    df['timestamp'] = pd.to_datetime(df['timestamp'],dayfirst=True)
    return df

#read 2 df 
df_features = read_secom()
df_target = read_labels()

#concat them vertically
df = pd.concat([df_features,df_target],axis=1)

df.head()


# In[40]:


df.drop_duplicates(keep=False)


# In[41]:


df.drop_duplicates()


# In[ ]:




