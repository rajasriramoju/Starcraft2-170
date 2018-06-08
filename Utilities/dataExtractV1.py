import numpy as np
import pandas as pd
from scipy import sparse

# import tensorflow as tf
# import keras
# from keras.models import Sequential
# from keras.layers import Dense
# from sklearn import preprocessing
import matplotlib.pyplot as mp

tot = 4334

fileNum = ""
currPath = ""

#initializing an empty matrix to contain the neural network data
NNMatrix = []

#loop for opening files
for i in range(tot):

	#creating the filename to open
	fileNum = str(i + 1)
	currPath = "./Protoss/" + fileNum + ".npz"
	print(currPath)

	#loading the entire numpy array from a file
	f = np.asarray(sparse.load_npz(currPath).todense())

	# This 1D array will consist the details of 1 game's
	matrixrow = []

	if (f[0,0] == 1):
		for colno in range(42):
			matrixrow.append(f[0, 71+(colno*6)])

		NNMatrix.append(matrixrow)

print(NNMatrix)
	

