#!/usr/bin/env python

#Imports
from mltools.tuning import tune, hp
import numpy as np

from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeRegressor

#Data Generation
N = 10000
X = np.ones((N, 2))
X[:,1] = range(N)
beta = np.array([10, -2])
y = X.dot(beta) + np.random.normal(0, 50, N)

#Estimator Class
estimator_class = DecisionTreeRegressor

#Splitting
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=70)

#Params-space definition
space = {
    'max_depth': hp.choice('max_depth', range(1, 4)),
    'min_samples_leaf': hp.choice('min_samples_leaf', range(10, 50, 5))
}

#Loss definition
def rmse(obs, pred):
    return np.sqrt(np.mean((obs-pred)**2))

#Tuning
best_params = tune(estimator_class, X_train, y_train, space, rmse, cv=5)
print "Best Params : ", best_params

#Fitting with best params
estimator = estimator_class(**best_params)
estimator.fit(X_train, y_train)

#Evaluation
train_pred = estimator.predict(X_train)
test_pred = estimator.predict(X_test)

train_err = rmse(y_train, train_pred)
test_err = rmse(y_test, test_pred)

print "Train Error: %.2f\nTest Error: %.2f" % (train_err, test_err)