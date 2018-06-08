import numpy as np
import pandas as pd
from scipy import sparse

import matplotlib.pyplot as mp

# Expects format of data according to https://github.com/wuhuikai/MSC
# Game data is stored in ../Protoss/####.npz format

# the total number of games we have at hand
tot = 4334

#init helper variables
fileNum = ""
currPath = ""

#extrapolated from https://github.com/wuhuikai/MSC/blob/master/parsed_replays/Stat/Protoss_human.json
units = [13, 1, 30, 16, 3, 36, 29, 2, 15, 24, 22, 34, 5, 8, 11, 7, 12, 35, 28]
unit_names = ['Probe','Zealot','Stalker','Sentry','Adept','High Templar','Dark Templar','Immortal','Colossus','Disruptor','Archon','Observer','Warp Prism','Phoenix','Void Ray','Oracle','Carrier','Tempest','Mothership']
#encoding units
unit_names_dict = {'Probe':1,'Zealot':2,'Stalker':3,'Sentry':4,'Adept':5,'High Templar':6,'Dark Templar':7,'Immortal':8,'Colossus':9,'Disruptor':10, 'Archon':11,'Observer':12,'Warp Prism':13,'Phoenix':14,'Void Ray':15,'Oracle':16,'Carrier':17,'Tempest':18,'Mothership':19}

#initializing an empty matrix to contain the neural network data
NNMatrix = []

#loop for opening files
for i in range(tot):

	#creating the filename to open
	fileNum = str(i + 1)
	currPath = "../Protoss/" + fileNum + ".npz"

	#loading the entire numpy array from a file
	f = np.asarray(sparse.load_npz(currPath).todense())
	shape = np.shape(f)

	#if the player won the game
	if (f[0,0] == 1):

		#init game matrix
		gamemat = []

		# redacted attempt to comppres data to a more managable size
		## for rowno in range(0, shape[0], 20):

		#iterates over each frame in the game matrix
		for rowno in range(0, shape[0]):
			#init frame with cumulative score
			frame = [f[rowno, 2]]
			#adds frameid, resource information, and
			for n in range(15, 25):
				frame.append(f[rowno, n])
			#init the differnces dictionary
			differences = {}
			#attach index to units and an end of game flag
			i = 0
			eog = False
			#iterates friendly ground and air units
			for u in units:
				#append the normalized count
				frame.append(f[rowno, 71 + u * 6])
				try:
					#create frame by frame dfferences for friendly units
					differences[unit_names[i]] = 0
					differences[unit_names[i]] = f[rowno + 1, 71 + u * 6] - f[rowno, 71 + u * 6]
				except:
					#end of game reached (rowno + 1 index)
					eog = True
					break
				#increment fo runits
				i += 1

			#iterates friendly ground and air units
			for u in units:
				#end of game reached (rowno + 1 index)
				if eog is True:
					break
				#append enemy unit counts
				frame.append(f[rowno, 317 + u * 6])
			#not end of game
			if eog is False:
				#name of unit with the max difference in count
				ma = max(differences, key = differences.get)
				if differences[ma] == 0.0:
					#append null encoding
					frame.append(0)
				else :
					#append some unit encoding
					frame.append(unit_names_dict[max(differences, key = differences.get)])
				# append entire frame to game matrix
				gamemat.append(frame)
		#append game matrix to neural net matrix
		NNMatrix.append(gamemat)

#save the entire labeled frame data matrix 
np.save("scoreResourcesFriendEnemy.npy", NNMatrix)
