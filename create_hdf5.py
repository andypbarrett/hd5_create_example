"""An example script to create a multi-dimensional HDF5 file"""

import h5py

shape = (5, 10)
dims = ["level", "point"]

f = h5py.File("test.h5", "w")
grp = f.create_group("Data")

# Create a temperature dataset with two dimensions
dset = grp.create_dataset("temperature", shape=shape, dtype="f")
dset.attrs["long_name"] = "air_temperature"
dset.attrs["units"] = "K"

# Testing
print(dset[:,:])
for attr_name, attr_value in dset.attrs.items():
    print(f"{attr_name}: {attr_value}")
