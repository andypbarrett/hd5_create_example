"""An example script to create a multi-dimensional HDF5 file"""

import h5py

shape = (5, 10)
dims = ["level", "point"]

f = h5py.File("test.h5", "w")
grp = f.create_group("Data")
dset = grp.create_dataset("temperature", shape=shape, dtype="f")

print(dset[:,:])

