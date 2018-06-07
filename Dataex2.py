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

units = [13, 1, 30, 16, 3, 36, 29, 2, 15, 24, 22, 34, 5, 8, 11, 7, 12, 35, 28]
unit_names = ['Probe','Zealot','Stalker','Sentry','Adept','High Templar','Dark Templar','Immortal','Colossus','Disruptor','Archon','Observer','Warp Prism','Phoenix','Void Ray','Oracle','Carrier','Tempest','Mothership']

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
	# print(currPath)

	#loading the entire numpy array from a file
	f = np.asarray(sparse.load_npz(currPath).todense())
	# This 1D array will consist the details of 1 game's
	#print(matrixrow)
	# matrixrow[0] = 0 -> this element is to be set the bias weight

	shape = np.shape(f)
	#qprint shape[0]
	# raw_input('?')

	if (f[0,0] == 1):
		gamemat = []
		for rowno in range(shape[0]):
			frame = [f[rowno, 2], f[rowno, 15:25]]
			differences = {}
			int i = 0
			bool eog = False
			for u in units:
				frame.append(f[rowno, 71 + u * 6])
				try:
					differences[unit_names[i]] = f[rowno + 1, 71 + u * 6] - f[rowno, 71 + u * 6]
				except:
					eog = True
					print("Reached the end of game.")
					break
				i++
			for u in units:
				if eog is True:
					break
				frame.append(f[rowno, 317 + u * 6])
			if eog is False:
				#max of units append
				frame.append(max(differences, key = differences.get))				
				gamemat.append(frame)

		NNMatrix.append(gamemat)

print(NNMatrix[0])
np.save("scoreResourcesFriendEnemy2.npy", NNMatrix)
	


#def find