import sys
import glob
import os
import numpy as np
from scipy import sparse

filelist = []
replays_array = []

for input_file in glob.glob("*.npz"):
  filelist.append(input_file)
  F = np.asarray(sparse.load_npz(input_file).todense())
  replays_array.append(F)

replays_array = np.asarray(replays_array)

print(np.shape(replays_array))
print(replays_array)
