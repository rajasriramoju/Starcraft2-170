import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.stats import beta
from scipy.stats import norm

# Splits data into intervals. Each interval is to be used to train a
# different Neural Network

# Basic way to create a beta distribution with parameters alpha and beta
# for separating intervals
## bet = beta(3,4)
## curve = np.arange(0.0, 1, .05)
## plt.plot(curve, bet.pdf(curve), linewidth=2.0)
## inter_vals = bet.cdf(np.arange(0, 1, .05))
## inter_vals[0] = 0.0
## print inter_vals

# Basic way to create a gaussian distribution with parameters mean and 
# variance for separating intervals
## nor = norm(loc=.3, scale=.3)
## curve = np.arange(0.0, 1, .05)
## plt.plot(curve, nor.pdf(curve), linewidth=2.0)
## inter_vals = nor.cdf(np.arange(0, 1, .05))
## inter_vals[0] = 0.0
## print inter_vals

# arranges 20 uniform intervals
inter_vals = np.arange(0, 1, .05)
# loads data
data = np.load("../scoreResourcesFriendEnemy.npy")
# 20 blank arrays
intervals = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

# iterates every game in the dataset
for game in data :
	shape = np.shape(game)
	# redacted attempt to consodlidate data
	## if shape[0] > 400 and shape[0] < 500 :

	# iterates through all frames game
	for i in range(shape[0]) :
		#calculates ratio
		no_frames = shape[0]
		ratio = float(i) / float(no_frames)

		# calculates interval index
		interval_index = 0
		for j in inter_vals :
			if ratio < j :
				break
			interval_index += 1

		# appends frame to interval
		intervals[interval_index - 1].append(game[i])

# saves intervals under a specified folder and name
for i in range(20):
	print np.shape(intervals[i])
	np.save('../IntervalsUniform4-5/intervalUniform4-5' + str(i) + '.npy', intervals[i])