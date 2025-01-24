#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

np.random.seed(42)
def createdata():
    data = {
        'Age':np.random.randint(18,70, size=20),
        'Salary':np.random.randint(3000, 239900, size=20),
        'Purchased':np.random.choice([0,1], size=20),
        'Gender':np.random.choice(['Male', 'Female'], size=20),
        'City':np.random.choice(['Newyork', 'San Franciso', 'Los Angeles'], size=20)
    }
    
    df = pd.DataFrame(data)
    return df
df = createdata()
df.head(10)


# In[2]:


df['Age_missing'] = df['Age'].isnull().astype(int)
df.head(10)


# In[6]:


from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
df['Gender'] = label_encoder.fit_transform(df['Gender'])
df.head()


# In[8]:


df = pd.get_dummies(df, columns=['City'], drop_first=True)
df.head()


# In[11]:


df = createdata()


# In[12]:


df['City'] = df['City'].map({'New York':1, 'San Francisco': 2, 'Los Angeles': 3})
df.head()


# In[11]:


import pandas as pd


# In[15]:


from sklearn.impute import SimpleImputer

def generate_example_database():
    data = {
        'PassengerId': [1, 2, 3, 4, 5],
        'Name': ['John', 'Jane', 'Bob', 'Alice', 'Charlie'],
        'Age': [22, None, 25, None, 30],
        'Fare': [7.25, 71.28, None, 8.05, 10.5],
        'Survived': [0, 1, 1, 0, 1]
    }
    return pd.DataFrame(data)
def clean_dataset(df):
    print("Original Dataset:")
    print(df)
    numeric_df = df.select_dtypes(include=['number'])
    imputer = SimpleImputer(strategy='mean')
    df_cleaned = pd.DataFrame(imputer.fit_transform(numeric_df), columns=numeric_df.columns)
    print("\nCleaned Dataset:")
    print(df_cleaned)
if __name__ == "_main_":
    df = generate_example_database()
    clean_dataset(df)


# In[ ]:





# In[ ]:




