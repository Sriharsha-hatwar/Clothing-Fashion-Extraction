from numpy import *;
array_len = 10000000
a = zeros(array_len, dtype=float)
import numpy as np
import h5py

data_to_write = np.random.random(size=(100,20)) # or some such

with h5py.File('name-of-file.h5', 'w') as hf:
    hf.create_dataset("name-of-dataset",  data=a)
	
with h5py.File('name-of-file.h5', 'r') as hf:
	data = hf['name-of-dataset'][:]
	print(len(data))
