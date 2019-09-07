#!/usr/bin/env python
# coding: utf-8

# In[26]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Import data
home_owner = pd.read_csv("home_ownership_data.csv")
loan_data = pd.read_csv("loan_data.csv")

#Parse the data
table = home_owner.merge(loan_data, how="inner", on="member_id")
table = table[['home_ownership', 'loan_amnt']]
table = table.groupby(['home_ownership']).mean()

#Export the table to CSV
table.to_csv("submission_csv.csv")

#Plot the data
plt.bar(table.index, table['loan_amnt'] )
plt.xlabel("Home Ownership", fontsize=12)
plt.ylabel("Loan Amount", fontsize=12)

plt.savefig("submission_plot_pdf.pdf")
plt.show()






