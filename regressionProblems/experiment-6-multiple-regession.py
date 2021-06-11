# Author: Prasad Chavan 19UME305
# Experiment No.: 06
# Title: Write a program for implementation of multiple variable regression.

import pandas as pd
from sklearn import linear_model

df = pd.read_csv('G:\kc_house_data.csv')

X = df[['bedrooms', 'sqft_living']]
y = df['price']

regr = linear_model.LinearRegression()
regr.fit(X, y)

#predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
predictedprice = regr.predict([[2, 1300]])

print(predictedprice)
