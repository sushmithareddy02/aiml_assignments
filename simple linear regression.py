#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf


# In[2]:


data1=pd.read_csv("NewspaperData.csv")
data1




# In[3]:


data1.info()


# In[4]:


data1.describe()



# In[5]:


plt.boxplot(data1["daily"])


# In[6]:


plt.scatter(data1["daily"],data1["sunday"])


# In[7]:


data1['daily'].corr(data1['sunday'])


# # #### Observations
# # - the relationship between x daily and y sunday is seen to be linear as seen from scatter plot
# # - the corr is strong and positive with pearsons corr coefficient of 0.95
# 

# In[8]:


model=smf.ols("sunday~daily",data=data1).fit()
model.summary()



# # #### observations 
# # - predicted equation is beta_0=13.8356,beta_1=1.3397 x
# # - beta_0+beta_1*x=y_hat
# # - The probability (p-value) for intercept(beta_0) is 0.707>0.05
# # - therefore the intercept coefficinet may not be that much significant in prediction
# # - however the p-value for 'daily'(beta_1) is 0.00<0.05
# # - therefore the beta_1 coefficinet is highly significant and id contributint to prediction.
# 

# In[9]:


x=data1["daily"].values
y=data1["sunday"].values
plt.scatter(x,y,color="m",marker="o",s=30)
b0=13.84
b1=1.33
y_hat=b0+b1*x
plt.plot(x,y_hat,color="g")
plt.xlabel('x')
plt.ylabel('y')
plt.show()


# In[10]:


x=data1['daily']
y=data1['sunday']
plt.scatter(data1['daily'],data1['sunday'])
plt.xlim(0,max(x)+100)
plt.ylim(0,max(y)+100)
plt.show()



# In[11]:


model1=smf.ols('sunday~daily',data=data1).fit()
model1.summary()


# In[12]:


model1.params


# In[13]:


print(f'model t-values:\n{model1.tvalues}\n--------------------\model p-values.\n{model1.pvalues}')


# In[14]:


#predict an new  data
newdata=pd.Series([200,300,1500])
data_pred=pd.DataFrame(newdata,columns=['daily'])
data_pred


# In[15]:


model1.predict(data_pred)



# In[16]:


#predict on all given training data
pred=model1.predict(data1['daily'])
pred


# In[17]:


#add predicted values as a collumns in data1
data1['y_hat']=pred
data1


# In[18]:


#compute the error values(residuals)and ass as another column
data1['residuals']=data1['sunday']-data1['y_hat']
data1


# In[19]:


mse=np.mean((data1['daily']-data1['y_hat'])**2)
rmse=np.sqrt(mse)
print("MSE:",mse)
print("RMSE:",rmse)


# In[20]:


plt.scatter(data1['y_hat'],data1['residuals'])


# #### Observations
# - there appears to be not trend and the residuals are randomly placed around the zero error line
# - hence the assumption of homoscedasticity is satisified(constant varriance in residuals)
# 

# In[22]:


import statsmodels.api as sm
sm.qqplot(data1['residuals'],line='45',fit=True)
plt.show()



# In[23]:


sns.histplot(data1['residuals'],kde=True)



# In[ ]:




