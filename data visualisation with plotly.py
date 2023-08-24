#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import pandas

import pandas as pd

# import plotly express

import plotly.express as px

# create a dataframe

accountancy_membership = pd.DataFrame({ 
              "Professional Bodies": ["ACCA","AICPA & CIMA","ICAEW", "CAI","ICAS", "CIPFA"],
              "Members (Including Students)": [783000, 689000, 202450, 31679, 23000, 14000]})

# create a plotly bar chart, specifying dataframe, x, y, title and colour arguments

fig = px.bar(data_frame=accountancy_membership,
             x ='Professional Bodies', 
             y ='Members (Including Students)',
             title = "Comparison of Accountancy Bodies Membership",
             color = 'Professional Bodies')

# show the bar chart

fig.show()


# In[ ]:




