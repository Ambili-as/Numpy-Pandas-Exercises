#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#ASSIGNMENT - NUMPY


# In[ ]:


#Exercise 1: (Score : 1)
#Create a numpy array containing the numbers from 1 to 10, and then reshape it to a 2x5 matrix.


# In[9]:


import numpy as np
array = np.arange(1,11)
matrix = array.reshape(2, 5)
print("Array: ")
print(array)
print("Reshaped matrix:")
print(matrix)


# In[ ]:


#Exercise 2: (Score : 1)
#Create a numpy array containing the numbers from 1 to 20, 
#and then extract the elements between the 5th and 15th index.


# In[1]:


import numpy as np
array = np.arange(1,21)
print(array)
elements = array[5:15]
print("Extracted elements: ", elements)


# In[ ]:


#Exercise 3: (Score : 2)
#Create a Pandas series with the following data: {'apples': 3, 'bananas': 2, 'oranges': 1}.
#Then, add a new item to the series with the key 'pears' and the value 4.


# In[8]:


import pandas as pd
fruits = pd.Series({'Apples':3,'Bananas':2,'Oranges':1})
print("original Fruits series:\n",fruits)
fruits['Pears'] = 4
print("Modified fruit Series:\n",fruits)


# In[ ]:


#Exercise 4: (Score : 2)
#Create a dataframe with the following columns: name, age, and gender.
#The dataframe should have 10 rows of data.


# In[22]:


import pandas as pd
data = {'Name':["Madhav","Ved","Mira","Mihika","Diva","Aryan","Shiva","Aishu","Aaru","Ammu"],
        "Age":[30,28,25,23,22,31,28,26,32,22],
        "Gender":["Male","Male","Female","Female","Female","Male","Female","Female","Female","Female"]}
df = pd.DataFrame(data)
df


# In[ ]:


#Exercise 5: (Score : 1)
#Add a new column to the data frame created in question 1, called occupation. 
#The values for this column should be Programmer, Manager, 
#and Analyst, corresponding to the rows in the dataframe.


# In[23]:


df["Occupation"] = ["Programmer","Manager","Analyst","Manager",
                      "Programmer","Manager","Analyst","Manager","Analyst","Programmer"]
df


# In[ ]:


#Exercise 6: (Score : 1)

#Select the rows of the dataframe where the age is greater than or equal to 30.


# In[24]:


Above_Thirty= df[df['Age']>=30]
print(Above_Thirty )


# In[ ]:


#Exercise 7: (Score : 2)
#Convert this dataframe to a csv file and read that csv file, 
#finally display the contents.


# In[25]:


df.to_csv('Details.csv')
print("Dataframe saved as Details.csv")
df_csv_read = pd.read_csv('Details.csv')
print(df_csv_read)


# In[ ]:




