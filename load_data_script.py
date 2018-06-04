import sys
import glob
import os
import numpy as np
import pandas as pd
from scipy import sparse
from keras.models import Sequential
from keras.layers import Dense
 
replays_array = []
df = pd.DataFrame(columns=['Game','Win','Frame ID','Minerals','Vespene','Food Cap','Food Used','Food Army','Food Worker','Idle Worker Count','Army Count','Warp Gate Count','Zealot','Immortal','Adept','Warp Prism','Oracle','Phoenix','Void Ray','Carrier','Probe','Colossus','Sentry','Archon','Disruptor','Mothership','Dark Templar','Stalker','Observer','Tempest','High Templar','Enemy Zealot','Enemy Immortal','Enemy Adept','Enemy Warp Prism','Enemy Oracle','Enemy Phoenix','Enemy Void Ray','Enemy Carrier','Enemy Probe','Enemy Colossus','Enemy Sentry','Enemy Archon','Enemy Disruptor','Enemy Mothership','Enemy Dark Templar','Enemy Stalker','Enemy Observer','Enemy Tempest','Enemy High Templar','Most Beneficial Unit'])

#this is where the files will be read into arrays then the arrays will be put into an array
int game_number = 1
for input_file in glob.glob("*.npz"):
  F = np.asarray(sparse.load_npz(input_file).todense())
  #process the frames and append onto frame
  df.loc[len(df)] = [game_number,F[0]] + F[15:24] + F[]
  replays_array.append(F)

replays_array = np.asarray(replays_array)

trimmed_games = []

for game in replays_array:
  for frame in game:
  
  

#neural network implementation
#probably 1 or 2 hiddne layers
#inputs depend on choices
#bias will involve cumulative score



print(np.shape(replays_array))
print(replays_array)
print(len(replays_array))
