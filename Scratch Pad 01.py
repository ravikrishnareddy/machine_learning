# List references
x = ['a', 'b', 'c']
y = x
y = x[0:2]
print(x, y)

# Numpy
import numpy as np
height = [1.61, 1.65, 1.69, 1.73, 1.77, 1.81]
weight = [40, 45, 50, 55, 60, 65]
height_np = np.array(height)
weight_np = np.array(weight)
bmi = weight_np/height_np**2
print(np.round(bmi,2))

# 2D array
height = np.round(np.random.normal(1.74, 0.20, 5000), 2)
weight = np.round(np.random.normal(72, 0.20, 5000), 2)
fam = np.column_stack((height, weight))
print(fam)

# Matplotlib pyplot
import matplotlib.pyplot as plt
year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]
plt.plot(year, pop)
plt.xlabel('year')
plt.ylabel('population')
plt.title('world population projections')
plt.yticks([0, 2, 4, 6, 8, 10], ['0', '2B', '4B', '6B', '8B', '10B'])
plt.show()


plt.scatter(year, pop)

values = [0, 0.6, 1.4, 1.6, 2.2, 2.5, 2.6, 3.2, 3.5, 3.9, 4.2, 6]
plt.hist(values, bins=3)

# Pandas
import pandas as pd
df = pd.read_csv('C:/Ravi Krishna Reddy/Data Science/Git/python/data/brics.csv', index_col=0)
display(df)
df.index
df.columns

# subset country column from brics using square brackets
brics = pd.read_csv('C:/Ravi Krishna Reddy/Data Science/Git/python/data/brics.csv', index_col=0)
brics['country']
type(brics['country'])
brics[['country']]
type(brics[['country']])
brics[['country', 'capital']]

# subset 2nd, 3rd and 4th row from brics dataframe
brics[1:4]

# subset russia row using loc
brics.loc['RU']
brics.loc['RU',]
brics.loc['RU',:]

# Filtering pandas dataframes
brics = pd.read_csv('C:/Ravi Krishna Reddy/Data Science/Git/python/data/brics.csv', index_col=0)
# Select countries with area greater than 8 million square kilometers
brics['country'][brics['area'] > 8]
# Select observations having area between 8 and 10 million square kilometers
brics[(brics['area']>8) & (brics['area']<10)]
import numpy as np
brics[np.logical_and(brics['area']>8, brics['area']<10)]

# Looping pandas dataframe
brics = pd.read_csv('C:/Ravi Krishna Reddy/Data Science/Git/python/data/brics.csv', index_col=0)
for i in brics:
    print(i)

for i, r in brics.iterrows():
    print(i)
    print(r)

for l, r in brics.iterrows():
    print(l + " : " + r['capital'])

for l, r in brics.iterrows():
    brics.loc[l, 'country_length'] = len(r['country'])
display(brics)

# Test code