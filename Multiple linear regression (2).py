#!/usr/bin/env python
# coding: utf-8

# In[14]:


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


# In[15]:


cars = pd.read_csv("Cars.csv")
cars.head()


# In[16]:


# Rearrange the columns
cars = pd.DataFrame(cars, columns=["HP","VOL","SP","WT","MPG"])
cars.head()


# #### Description of columns
# - MPG : Milege of the car (Mile per Gallon)
# - HP : Horse Power of the car  
# - VOL : Volume of the car (Size)
# - SP : Top speed of the car (Miles per Hour)
# - WT : Weight of the car (Pounds)

# In[17]:


cars.isna().sum()


# #### Obervations
# - There are no missing values
# - There are 81 observations
# - The data types in each columns are relevant and valid

# In[18]:


fig, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (.15, .85)})
sns.boxplot(data=cars, x='HP', ax=ax_box, orient='h')
ax_box.set(xlabel='')
sns.histplot(data=cars, x='HP', ax=ax_hist, bins=30, kde=True, stat="density")
ax_hist.set(ylabel='Density')
plt.tight_layout()
plt.show()


# In[19]:


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

# In[20]:


cars[cars.duplicated()]


# In[21]:


sns.set_style(style='darkgrid')
sns.pairplot(cars)


# In[22]:


cars.corr()


# #### Observations from correlation plots and coeffcients
# - Between x and y, all the x variables are showing moderate to high correlation strengths, highest being between HP nad MPG
# - Therefotre this dataset qualifies for building a multiple linear regression model to predict MPG
# - Among x columns (x1,x2,x3, and,x4), some very high correlation strength are observed between SP vs HP, VOL vs WT

# #### Preparing a preliminary model cosidering all X columns

# In[28]:


model1 = smf.ols('MPG~WT+VOL+SP+HP',data=cars).fit()


# #### Observations from model summary
# - The R-squared and adjusted R-suared values are good and about 75% of variability in Y explained by X columns
# - The probabnility value with respect to F-statistic is close to zero, indicating that all or some of X columns qare significant
# - The P- vale for VOLand WT are higher than 5% indicating some interaction issue among themeselves, which need to be further explored

# #### Performance metrices for mode1

# In[29]:


df1 = pd.DataFrame()
df1["actual_y1"] = cars["MPG"]
df1.head()


# In[30]:


pred_y1 = model1.predict(cars.iloc[:,0:4])
df1["pred_y1"] = pred_y1
df1.head()


# In[35]:


from sklearn.metrics import mean_squared_error
mse =  mean_squared_error(df1["actual_y1"], df1["pred_y1"])
print("MSE : ", mse)
print("RMSE :",np.sqrt(mse))


# In[36]:


cars.head()


# In[37]:


# Compute VIF values
rsq_hp = smf.ols('HP~WT+VOL+SP',data=cars).fit().rsquared
vif_hp = 1/(1-rsq_hp)

rsq_wt = smf.ols('WT~HP+VOL+SP',data=cars).fit().rsquared  
vif_wt = 1/(1-rsq_wt) 

rsq_vol = smf.ols('VOL~WT+SP+HP',data=cars).fit().rsquared  
vif_vol = 1/(1-rsq_vol) 

rsq_sp = smf.ols('SP~WT+VOL+HP',data=cars).fit().rsquared  
vif_sp = 1/(1-rsq_sp) 

# Storing vif values in a data frame
d1 = {'Variables':['Hp','WT','VOL','SP'],'VIF':[vif_hp,vif_wt,vif_vol,vif_sp]}
Vif_frame = pd.DataFrame(d1)  
Vif_frame


# In[ ]:




