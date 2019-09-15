dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

import pandas

brics = pandas.DataFrame(dict)
print(brics, "\n")

# Set the index for brics
brics.index = ["BR", "RU", "IN", "CH", "SA"]
print(brics, "\n")

# Read csv data
random = pandas.read_csv("random.csv")
print(random, "\n")

# Indexing data frames

       # You can use square brackets to select one column of the random DataFrame. You can either use a single bracket or a double bracket.
       # The single bracket with output a Pandas Series, while a double bracket will output a Pandas DataFrame.

# Print out unit column as Pandas Series
print( random['unit'], '\n')

# Print out unit column as Pandas DataFrame
print( random[['unit']], '\n' )

# Print out DataFrame with unit and home
print( random[['unit', 'home']] , '\n')

# Print out first 4 rows(observations) from a DataFrame
print( random[0:4], '\n' )

random2 = pandas.read_csv("random.csv", index_col=0)
# Print out row 4 to 6 from a DataFrame
print( random[4:6], '\n')
print( random2[4:6], '\n')

# You can also use loc and iloc to perform just about any data selection operation.
# loc is label-based, which means that you have to specify rows and columns based on their row and column labels.
# iloc is integer index based, so you have to specify rows and columns by their integer index

print( random.iloc[2] , '\n')
