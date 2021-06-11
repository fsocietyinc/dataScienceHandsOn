# Author: Prasad Chavan 19UME305
# Experiment 9: Implementation of Naïve Bays Classifier.


#importing required modules
import numpy as np
import pandas as pd
#Reading data
data=pd.read_csv('play_golf.csv')
data.head()
data.drop(columns=['day'], inplace=True)
print(data)
print('\n')
#counting totals of yes and no
print('total of\n ' ,data['play'].value_counts())
print('\n')

#probabilities of yes and no
py = 9/14
pn = 5/14

print('probability of Yes=', py)
print('probability of NO=',pn)
print('\n')
#outlook
print('Frequency Distribution of outlook \n',pd.crosstab(data['outlook'], data['play']))
print('\n')
pOverNo= 0
pRainNo= 2/5
pSunnyNo= 3/5

pOverY= 4/9
pRainY= 3/9
pSunnyY= 2/9

#temp
print('Frequency Distribution of temp \n',pd.crosstab(data['temp'], data['play']))
print('\n')
pCoolNo= 1/5
pHotNo= 2/5
pMildNo= 2/5

pCoolY= 3/9
pHotY= 2/9
pMildY= 4/9

#humidity
print('Frequency Distribution of humidity \n',pd.crosstab(data['humidity'], data['play']))
print('\n')
pHighNo= 4/5
pNorNo= 1/5

pHighY= 3/9
pNorY= 6/9

#wind
print('Frequency Distribution of wind \n',pd.crosstab(data['wind'], data['play']))
print('\n')
pStrNo= 3/5
pWeakNo= 2/5

pStrY= 3/9
pWeakY= 6/9


#prediction 
# For Outlook = Rainy, Temp = cool, Humidity = high, wind = strong
pYes = py *pRainY *pCoolY *pHighY *pStrY
pNo = pn *pRainNo *pCoolNo *pHighNo *pStrNo

if pYes > pNo:
    print('Play = True')
    
else :
    print('Play = False')