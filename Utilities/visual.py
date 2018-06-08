import numpy as np

data = np.load("../scoreResourcesFriendEnemy.npy")

print np.shape(data[3])
for frame in data[3] :
	print frame[-1]