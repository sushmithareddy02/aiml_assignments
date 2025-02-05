#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Assumptions in Multilinear Regression
1.Linearity: The relationship between the predictors and thea response is linear
2.Independence: Observations are independent of each other


# In[7]:


import pandas as pd  
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf
from statsmodels.graphics.regressionplots import influence_plot
import numpy as np


# In[8]:


cars = pd.read_csv("Cars.csv")
cars.head()


# In[10]:


# Rearrange the columns
cars = pd.DataFrame(cars, columns=["HP","VOL","SP","WT","MPG"])
cars.head()


# #### Description of columns
# - MPG : Milege of the car (Mile per Gallon)
# - HP : Horse Power of the car  
# - VOL : Volume of the car (Size)
# - SP : Top speed of the car (Miles per Hour)
# - WT : Weight of the car (Pounds)

# In[11]:


cars.isna().sum()


# #### Obervations
# - There are no missing values
# - There are 81 observations
# - The data types in each columns are relevant and valid

# In[12]:


fig, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (.15, .85)})
sns.boxplot(data=cars, x='HP', ax=ax_box, orient='h')
ax_box.set(xlabel='')
sns.histplot(data=cars, x='HP', ax=ax_hist, bins=30, kde=True, stat="density")
ax_hist.set(ylabel='Density')
plt.tight_layout()
plt.show()


# In[13]:


fig, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (.15, .85)})
sns.boxplot(data=cars, x='VOL', ax=ax_box, orient='h')
ax_box.set(xlabel='')
sns.histplot(data=cars, x='VOL', ax=ax_hist, bins=30, kde=True, stat="density")
ax_hist.set(ylabel='Density')
plt.tight_layout()
plt.show()


# #### Observations from boxplot and histograms
# - There are some extreme values(outliers) observed in towards the right tail of Sp and Hp distributions
# - in VOL and WT columns , a few outliers are observed in both tails oh their distributions.
# - The extreme values of cars data may have come from specially designed nature of cars
# - As this is multi-dimensional

# In[15]:


cars[cars.duplicated()]


# In[17]:


sns.set_style(style='darkgrid')
sns.pairplot(cars)


# In[18]:


cars.corr()


# #### Observations from correlation plots and coeffcients
# - Between x and y, all the x variables are showing moderate to high correlation strengths, highest being between HP nad MPG
# - Therefotre this dataset qualifies for building a multiple linear regression model to predict MPG
# - Among x columns (x1,x2,x3, and,x4), some very high correlation strength are observed between SP vs HP, VOL vs WT

# #### Preparing a preliminary model cosidering all X columns

# In[26]:


model1 = smf.ols('MPG~WT+VOL+SP+HP',data=cars).fit()


# In[27]:


model1.summary()


# In[ ]:




