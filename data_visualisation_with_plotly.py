import pandas as pd

import plotly.express as px
accountancy_membership = pd.DataFrame({ 
              "Professional Bodies": ["ACCA","AICPA & CIMA","ICAEW", "CAI","ICAS", "CIPFA"],
              "Members (Including Students)": [783000, 689000, 202450, 31679, 23000, 14000]})
fig = px.bar(data_frame=accountancy_membership,
             x ='Professional Bodies', 
             y ='Members (Including Students)',
             title = "Comparison of Accountancy Bodies Membership",
             color = 'Professional Bodies')
fig.show()
