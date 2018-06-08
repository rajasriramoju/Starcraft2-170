import keras
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import pandas as pd

X = argv[1]
Y = argv[2]

msk = np.random.rand(len(X)) < 0.8

train_X = X[msk]
train_Y = Y[msk]

test_X = X[~msk]
test_Y = Y[~msk]

model = Sequential()

model.add(Dense(49, input_dim=49, activation='relu'))
model.add(Dense(49, activation='relu'))
model.add(Dense(49, activation='relu'))

model.add(Dense(1))

model.compile(loss='mean_squared_error', optimizer='adam')

model.fit(train_X, train_Y, epochs=1000)
		
model.evaluate(test_X)

print model.predict(np.array([[0,0]]))