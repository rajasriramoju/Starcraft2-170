import keras
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import pandas as pd

#train and test should be type of pandas dataframe
def NeuralNetwork(train, test):
        #Defining layers with input layer having 49 inputs, activation functions are relu.
        model = Sequential()
        model.add(Dense(49, activation='relu', input_dim=49))
        model.add(Dense(49, activation='relu'))
        model.add(Dense(49, activation='relu'))

        #Defining output layer with 1 output.
        model.add(Dense(1))

        #Defining metrics and optimizer for the model.
        model.compile(loss='mean_squared_error', optimizer='adam', metrics= ['acc'])

        #Train set x processed to have only first 49 columns, train set y processed to containing only last column.
        train_arr_x = train.drop(columns=['Most Beneficial Unit']).values
        train_arr_y = train['Most Beneficial Unit'].values

        #Same process for test set x and y.
        test_arr_x = test.drop(columns=['Most Beneficial Unit']).values
        test_arr_y = test['Most Beneficial Unit'].values

        #Training NN
        model.fit(train_arr_x, train_arr_y, batch_size=50, epochs=1000)

        #Output the metrics defined in compile
        print(model.evaluate(test_arr_x, test_arr_y))
