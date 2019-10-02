
# coding: utf-8

# In[60]:


import pandas as  pd
df = pandas.read_csv(r"C:\Users\Chandrima\Desktop\Book1.csv")
pd.set_option('display.max_rows', 151)
print (df)


# In[48]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df = pd.read_csv(r"C:\Users\Chandrima\Desktop\Book1.csv")
sns.lmplot(x="SepalLength", y="SepalWidth", data=df, hue='Species', fit_reg=False)
plt.show()


# In[61]:


import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\Chandrima\Desktop\Book1.csv")
irisplot = sns.PairGrid(df, hue="Species")
irisplot.map(plt.scatter);
irisplot.savefig ("irisPlot.png")
irisplot.fig.subplots_adjust(top=0.9)
irisplot.fig.suptitle('Iris Dataset Visualization', fontsize=16)

