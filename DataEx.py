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


for i in range(5):
	
	#f = np.asarray(sparse.load_npz('./Protoss/4.npz').todense())
	fileNum = str(i + 1)
	currPath = "./Protoss/" + fileNum + ".npz"
	print(currPath)
	f = np.asarray(sparse.load_npz(currPath).todense())
	print(f[0,0])
	
	
	
	


def find