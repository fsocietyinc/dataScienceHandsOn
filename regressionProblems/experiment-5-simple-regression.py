# Author: Prasad Chavan 19UME305
# Experiment No.: 05
# Title: Write a program for implementation of simple linear regression.

import numpy as np
import matplotlib.pyplot as plt

def hypothesisFunction(X, theta):
    
    return np.dot(X, theta)

def costFunction(y_predicted, y):
    
    m = y.size
    return (1/(2*m))*np.sum(np.square(np.subtract(y_predicted,y)))

def initializeTheta(n):
    return np.zeros((n,1))

def updateTheta(theta, alpha, y, y_predicted, X):
    
    m = y.size
    theta[0] = theta[0] - (alpha/m)*np.sum(np.subtract(y_predicted,y))
    theta[1] = theta[1] - (alpha/m)*np.sum(np.multiply(np.subtract(y_predicted,y), X[:,1]))
    return theta

x = [1000, 1120, 1250, 1400, 1500]
y = [118000,125000,130000,150000,165000]

xStd = np.std(x)
xMean = np.mean(x)
x_scaled = (x - xMean)/xStd

m = len(y)
n = 2

X = np.zeros((m,n))
X[:,0] = 1
X[:,1] = x_scaled

y = np.array(y)

yStd = np.std(y)
yMean = np.mean(y)
y_scaled = (y - yMean)/yStd

theta = initializeTheta(n)
epochs = 100
alpha = 0.0000000000000000005

costs = []
thetas = []

for _ in range(epochs):
    
    y_predicted = hypothesisFunction(X, theta)
    cost = costFunction(y_predicted, y_scaled)
    costs.append(cost)
    theta = updateTheta(theta, alpha, y_scaled, y_predicted, X)
    thetas.append(theta)

costs = np.array(costs)
plt.figure()
plt.plot(costs)
plt.xlabel('Epoch')
plt.ylabel('Cost')
plt.show()

X_test = np.array([1,1300])

y_test = hypothesisFunction(X_test, theta)
y_test = y_test*yStd + yMean
print(y_test)

