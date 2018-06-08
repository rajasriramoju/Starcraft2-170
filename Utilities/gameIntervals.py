import numpy as np
from scipy import beta
from scipy import norm

# A simple method of extrapolating a game's data from 
# the over arching data structure

# creates the 20 uniform intervals
inter_vals = np.arange(0, 1, .05)
# loads the data from the 
data = np.load("../scoreResourcesFriendEnemy.npy")

# 20 blank interval arrays
intervals = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
# gets game 1000 from the total array
game = data[999];
shape = np.shape(game)
# iterates over every frame in the game
for i in range(shape[0]) :
	# computes ration of progress through the game
	no_frames = shape[0]
	ratio = float(i) / float(no_frames)

	# finds the proper interval for a ratio
	interval_index = 0
	for j in inter_vals :
		if ratio < j :
			break
		interval_index += 1

	# places frame in that interval
	intervals[interval_index - 1].append(game[i])

# saves every interval of data from the game
for i in range(20):
	np.save('../game1000/intervalGame1000Uniform_.1' + str(i) + '.npy', intervals[i])