#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data = {
    'Name': ['John', 'Alice', 'Bob', 'Diana'],
    'Age': [28, 34, 23, 29],
    'Department': ['HR', 'IT', 'Marketing', 'Finance'],
    'Salary': [45000, 60000, 35000, 50000]
}


df = pd.DataFrame(data)
print(df)


# In[2]:


import pandas as pd

data = {
    'Name': ['John', 'Alice', 'Bob', 'Diana'],
    'Age': [28, 34, 23, 29],
    'Department': ['HR', 'IT', 'Marketing', 'Finance'],
    'Salary': [45000, 60000, 35000, 50000]
}
df = pd.DataFrame(data)

print("First 2 rows of the DataFrame:")
print(df.head(2))

df['Bonus'] = df['Salary'] * 0.10
print("\nDataFrame after adding Bonus column:")
print(df)


average_salary = df['Salary'].mean()
print("\nAverage salary of employees:", average_salary)


employees_older_than_25 = df[df['Age'] > 25]
print("\nEmployees older than 25:")
print(employees_older_than_25)


# In[ ]:




