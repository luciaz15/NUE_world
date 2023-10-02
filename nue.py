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
plt.title("Evolution of world yield data from 1961 to 2017")
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