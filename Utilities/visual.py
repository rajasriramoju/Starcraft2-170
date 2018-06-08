import numpy as npx	
from keras.models import load_model

# Displays a visual method to see how well a prediction model fits the
# actual label

# unit names encoding for 
unit_names_dict = {'Null':0, 'Probe':1,'Zealot':2,'Stalker':3,'Sentry':4,'Adept':5,'High Templar':6,'Dark Templar':7,'Immortal':8,'Colossus':9,'Disruptor':10, 'Archon':11,'Observer':12,'Warp Prism':13,'Phoenix':14,'Void Ray':15,'Oracle':16,'Carrier':17,'Tempest':18,'Mothership':19}

# iterate over all intervals in game 1000
for i in range(20):
	# load the interval
	data = np.load("../game1000/intervalGame1000Uniform_.1" + str(i) + ".npy")
	# load the model to predict the known label
	model = load_model('../IntervalUniform_.1/intervalUniform_.1' + str(1) + ".h5")
	print "New Interval ===================== Size:" + str(np.shape(data)) + "  " + str(i)
	print model.predict(data[:, 0:-1])
	# prints the label
	for frame in data :
		print unit_names_dict.keys()[unit_names_dict.values().index(frame[-1])]

