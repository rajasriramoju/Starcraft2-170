import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.stats import norm

bet = norm(loc=.5, scale=.2)
# curve = np.arange(0.0, 1, .05)

# plt.plot(curve, bet.pdf(curve), linewidth=2.0)
# plt.show()

inter_vals = bet.cdf(np.arange(0, 1, .1))
inter_vals[0] = 0.0
print inter_vals


data = np.load("scoreResourcesFriendEnemy.npy")

intervals = [[], [], [], [], [], [], [], [], [], []]

for game in data :

	shape = np.shape(game)

	for i in range(shape[0]) :

		no_frames = shape[0]
		ratio = float(i) / float(no_frames)

		interval_index = 0
		for j in inter_vals :
			if ratio < j :
				break
			interval_index += 1

		# print interval_index
		# raw_input()

		intervals[interval_index - 1].append(game[i])

for i in range(10):
	intervals[i].save('interval' + str(i) + '.npy')