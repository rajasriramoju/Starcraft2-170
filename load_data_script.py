import sys
import glob
import os
import keras
import numpy as np
import pandas as pd
from scipy import sparse
from keras.models import Sequential
from keras.layers import Dense
#pretty printing dataframe
from tabulate import tabulate

#this is where the files will be read into arrays then the arrays will be put into an array
for input_file in glob.glob("*.npy"):
	data = np.load(input_file)
	column_names = np.array(['Cumulative','Frame ID','Minerals','Vespene','Food Cap','Food Used','Food Army','Food Worker','Idle Worker Count','Army Count','Warp Gate Count','Probe','Zealot','Stalker','Sentry','Adept','High Templar','Dark Templar','Immortal','Colossus','Disruptor','Archon','Observer','Warp Prism','Phoenix','Void Ray','Oracle','Carrier','Tempest','Mothership','Enemy Probe','Enemy Zealot','Enemy Stalker','Enemy Sentry','Enemy Adept','Enemy High Templar','Enemy Dark Templar','Enemy Immortal','Enemy Colossus','Enemy Disruptor','Enemy Archon','Enemy Observer','Enemy Warp Prism','Enemy Phoenix','Enemy Void Ray','Enemy Oracle','Enemy Carrier','Enemy Tempest','Enemy Mothership','Most Beneficial Unit'])
	np.concatenate([column_names,data])
	#process the frames and append onto frame
	df = pd.DataFrame(data=data[1:,1:],    # values
	    # 1st column as index
	columns=data[0,:])  # 1st row as the column names
	#print tabulate(df2, headers='keys', tablefmt='psql')
	print(df2)
	#neural network implementation
	#probably 1 or 2 hiddne layers
	#inputs depend on choices
	#bias will involve cumulative score
'''
	msk = np.random.rand(len(X)) < 0.8

	train_X = X[msk]
	train_Y = Y[msk]

	test_X = df[~msk]
	test_Y = df[~msk]

	model = Sequential()

	model.add(Dense(49, activation='relu'))
	model.add(Dense(49, activation='relu'))
	model.add(Dense(49, activation='relu'))

	model.add(Dense(1))

	model.compile(loss='mean_squared_error', optimizer='adam')

	model.fit(train_X, train_Y, epochs=1000)

	model.evaluate(test_X)

	print model.predict(np.array([[0,0]]))
'''
