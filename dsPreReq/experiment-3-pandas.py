# Author: Prasad Chavan 19UME305
# Experiment 3: Implementation of exploratory data analysis using Pandas dataframes.

import pandas as pd, numpy as np 

# The basic method to create a Series is to call:
# s = pd.Series(data, index=index)

# When the data is a dict, and an index is not passed, the Series index will be ordered by
# the dict’s insertion order
d = {'b': 1, 'a': 0, 'c': 2}
ds = pd.Series(d)
print(ds)

#If data is an ndarray, index must be the same length as data. If no index is passed,
# one will be created having values [0, ..., len(data) - 1]
s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
print(s)

# If data is a scalar value, an index must be provided. The value will be repeated to
# match the length of index.
sclr = pd.Series(5., index=['a', 'b', 'c', 'd', 'e'])
print(sclr)


# DataFrames

# DataFrame From dict of Series or dicts
d = {'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']), 'two': pd.Series([1., 2., 3., 4.],
index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print(df)

# DataFrame from dict of ndarrays / lists
d = {'one': [1., 2., 3., 4.], 'two': [4., 3., 2., 1.] }
da = pd.DataFrame(d)
print(da)

# DataFrame from structured or record array
data = np.zeros((2, ), dtype=[('A', 'i4'), ('B', 'f4'), ('C', 'a10')])
data[:] = [(1, 2., 'Hello'), (2, 3., "World")]
d_arr = pd.DataFrame(data)
print(d_arr)
