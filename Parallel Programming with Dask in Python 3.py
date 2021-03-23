#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt

# Multiple CSV files of flight information have been provided from the 
# Bureau of Transportation Statistics. Each file contains one month of information in 2016 (Jan to May).

# 1. build a function to compute the percentage of delayed flights given a DataFrame of flight information. Your function will 
# take a single DataFrame as input and compute the percentage of its rows in which the 'DEP_DELAY' value is greater than zero.

# Define function with single input called df: pct_delayed
def pct_delayed(df):
    # Compute number of delayed flights: n_delayed
    n_delayed = (df['DEP_DELAY']>0).sum()
    # Return percentage of delayed flights
    return n_delayed  * 100 / len(df) 

# 2. Apply it with a generator to analyze the percentage of delayed flights for 
#    each month ('Jan','Feb','Mar','Apr','May') of 2016.

template='flightdelays-2016-{:01d}.csv'
filenames=[template.format(k) for k in range(1,6)]

# Define the generator: dataframes
dataframes = (pd.read_csv(file) for file in filenames)

# Create the list comprehension: monthly_delayed
monthly_delayed = [pct_delayed(df) for df in dataframes]

# Create the plot
x=['Jan','Feb','Mar','Apr','May']
plt.plot(x, monthly_delayed, marker='o', linewidth=1)
plt.ylabel('% Delayed')
plt.xlabel('Months - 2016')
plt.xlim((-1,5))
plt.ylim((0,100))
plt.title('% of delays the first 5 months of 2016')
plt.show()


# In[ ]:




