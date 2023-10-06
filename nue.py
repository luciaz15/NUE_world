import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('cereal-crop-vs-fertilizer-application.csv')


# iterating the columns
for col in data.columns:
    print(col)

#Change name of the columns:
data.columns.values[3] = 'Yield'
data.columns.values[4] = 'Nitrogen'

print('Original NUE data')
print(data)

#Filter world data for entity
newdf = data[(data.Entity == "World")]
print('Filter NUE world data')
print(newdf)

# scatter plot title
plt.title("Evolution of world yield data from 1961 to 2017")
plt.xlabel("Year")
plt.ylabel("Yield (tonnes per hectare)")
plt.scatter(x=newdf.Year, y=newdf.Yield)
plt.show()

#plot witht a line
plt.plot(newdf['Year'], newdf['Yield'], linestyle = 'dotted', c='hotpink')
plt.suptitle("Evolution of world yield data from 1961 to 2021")
plt.tile("Clearer dots shows more recent years")
plt.xlabel("Year")
plt.ylabel("Yield (tonnes per hectare)")
plt.show()

#Draw regression line
import matplotlib.pyplot as plt
from scipy import stats

slope, intercept, r, p, std_err= stats.linregress(newdf['Year'],newdf['Yield'])

def myfunc(x):
    return slope * x + intercept
mymodel= list(map(myfunc, newdf['Year']))

plt.scatter(newdf['Year'],newdf['Yield'])
plt.plot(newdf['Year'], mymodel)
plt.show()

# Start plotting Nitrogen use vs yield as colormap

#filter only from Y2K
newdf.info()

#Filter world data for entity
newdf1 = newdf[(newdf.Year >= 2001)&(newdf.Year < 2021)]

#dataframe["date"] = pd.to_datetime(dataframe["date"]) 

plt.scatter(newdf1['Nitrogen'],newdf1['Yield'], c =newdf1['Year'])
plt.suptitle ('Evolution of nitrogen use effiency from 2002 to 2021')
plt.title("Clearer dots shows more recent years")
plt.xlabel("Nitrogen use (kg.ha-1)")
plt.ylabel("Yield (t.ha-1)")
plt.colorbar()
plt.show()

import numpy as np

#Create a new column to measure the efficiency
wordl_eff_2001 = print(newdf1.iloc[1]['Efficiency'])

#Define conditions for an overview of the evolution of the nitrogen use efficiency since 2001
conditions = [
    (newdf1['Efficiency']== newdf1.iloc[0]['Efficiency']),
    (newdf1['Efficiency'] < newdf1.iloc[0]['Efficiency']),
    (newdf1['Efficiency'] > newdf1.iloc[0]['Efficiency']),
]

#define results
results= ['Stable','Decrease','Increase']

#Create new column based on conditions
newdf1['Eff_relative'] = np.select(conditions, results)

#plot the above information
import plotly.express as px

fig = px.scatter(newdf1, x='Nitrogen', y='Yield', text ='Year', color='Eff_relative')
fig.update_traces (textposition = 'top center')
fig.update_layout (title_text= 'Evolution of nitrogen use effiency from 2002 to 2021')
fig.show()

#plot box of Australia, Brazil, China, France, India, United States
import plotly.express as px
#Filter world data for entity
df= data[(data.Year >= 2001) & (data.Year < 2021)]
df_top5 = df.loc[df['Entity'].isin(['Australia', 'Brazil', 'China', 'France', 'India', 'United States'])]

#Create a new column to measure the efficiency
df_top5['Efficiency'] = df_top5['Yield']/df_top5['Nitrogen']

#Create the boxplot
fig = px.box(df_top5, x='Entity', y='Efficiency', points ='all', labels= { "Entity": "Country", "Efficiency": "NUE (t of cereals per kg N)"})
fig.update_layout (title_text= 'Comparison of nitrogen use efficiency (NUE)')

fig.show()

#Highlight only one country
import plotly.express as px

df['Efficiency'] = df['Yield']/df['Nitrogen']

plot_df = df.dropna()

fig= px.scatter(df_top5, x= "Nitrogen", y="Yield", color='Entity', size='Efficiency')
fig.show()
