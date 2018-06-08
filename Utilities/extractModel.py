import sys
import numpy as np
import pandas as pd
from modelTemplate import NeuralNetwork

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

	#Neural Network
	
	NeuralNetwork(train,test)

Main(sys.argv[1])
