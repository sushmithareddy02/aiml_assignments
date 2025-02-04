#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Assumptions in Multilinear Regression
1.Linearity: The relationship between the predictors and thea response is linear
2.Independence: Observations are independent of each other


# In[2]:


import pandas as pd  
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf
from statsmodels.graphics.regressionplots import influence_plot
import numpy as np


# In[3]:


cars = pd.read_csv("Cars.csv")
cars.head()


# In[5]:


# Rearrange the columns
cars = pd.DataFrame(cars, columns=["HP","VOL","SP","WT","MPG"])
cars.head()


# #### Description of columns
# - MPG : Milege of the car (Mile per Gallon)
# - HP : Horse Power of the car  
# - VOL : Volume of the car (Size)
# - SP : Top speed of the car (Miles per Hour)
# - WT : Weight of the car (Pounds)

# In[6]:


cars.isna().sum()


# #### Obervations
# - There are no missing values
# - There are 81 observations
# - The data types in each columns are relevant and valid

# In[8]:


fig, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (.15, .85)})
sns.boxplot(data=cars, x='HP', ax=ax_box, orient='h')
ax_box.set(xlabel='')
sns.histplot(data=cars, x='HP', ax=ax_hist, bins=30, kde=True, stat="density")
ax_hist.set(ylabel='Density')
plt.tight_layout()
plt.show()


# In[ ]:




