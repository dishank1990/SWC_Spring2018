
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import pandas as pd
my_file = pd.read_table("gapminder.txt")
# Subsetting
Canada = my_file.loc[my_file['country']== "Canada"]
# Plotting
Canada.plot.line(x='year',y='lifeExp', label='Life expectency', figsize=(8,6))
plt.suptitle("Life expectency in canada over the years", fontsize = 20)
plt.xlabel("year", fontsize =16)
plt.ylabel("Life expectency", fontsize = 16)
plt.savefig("PlotLifeExp.png")

