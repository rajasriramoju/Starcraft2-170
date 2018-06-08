import sys
import glob
import keras
import numpy as np
import pandas as pd
from scipy import sparse
from keras.models import Sequential
from keras.layers import Dense

def Main(input_file):
	#Dataframe Column Names
	column_names = ['Cumulative','Frame ID','Minerals','Vespene','Food Cap','Food Used','Food Army','Food Worker','Idle Worker Count','Army Count','Warp Gate Count','Probe','Zealot','Stalker','Sentry','Adept','High Templar','Dark Templar','Immortal','Colossus','Disruptor','Archon','Observer','Warp Prism','Phoenix','Void Ray','Oracle','Carrier','Tempest','Mothership','Enemy Probe','Enemy Zealot','Enemy Stalker','Enemy Sentry','Enemy Adept','Enemy High Templar','Enemy Dark Templar','Enemy Immortal','Enemy Colossus','Enemy Disruptor','Enemy Archon','Enemy Observer','Enemy Warp Prism','Enemy Phoenix','Enemy Void Ray','Enemy Oracle','Enemy Carrier','Enemy Tempest','Enemy Mothership','Most Beneficial Unit']

	#Load input file into numpy array and load array into dataframe.
	data = np.load(input_file)
	df = pd.DataFrame(data, columns = column_names)
	
	#Train and Test set split using numpy randomizer.
	#Train set is 75% of the dataframe.
	#Test set is 25% of the dataframe.
	msk = np.random.rand(len(df)) < 0.76
	train = df[msk]
	test = df[~msk]

	#Neural Network Implementation

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

Main(sys.argv[1])
