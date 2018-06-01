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
 
# #f = np.asarray(sparse.load_npz('./Protoss/4.npz').todense())
# shp = f.shape
# print(shp[0])
# w = f[490:500,105:125]
# print(w)

fileNum = ""
currPath = ""

# NN matrix needs 41 columns
# Matrixtest = [[0 for a in range(3)] for b in range(10)]  -> creates 10 rows and 3 colummns ->for reference

#NNmatrix = [[for colno in range(41)] ]

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
	# print(f[0,0])

	# This 1D array will consist the details of 1 game's
	matrixrow = []
	#print(matrixrow)
	# matrixrow[0] = 0 -> this element is to be set the bias weight

	if (f[0,0] == 1):
		for colno in range(42):
			matrixrow.append(f[0, 71+(colno*6)])

		NNMatrix.append(matrixrow)

print(NNMatrix)
	
	


#def find