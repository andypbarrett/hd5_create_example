"""An example script to create a multi-dimensional HDF5 file"""

import numpy as np
import h5py

filename = "test.h5"
shape = (5, 10)
dims = ["level", "point"]

# Create a file with one group and two 2D datasets
with h5py.File(filename, "w") as f:
    grp = f.create_group("Data")

    # Create dimension variables
    level = grp.create_dataset("level", shape=(5,), dtype="f")
    level[:] = [1000., 925., 850., 700., 500.]
    level.attrs["long_name"] = "pressure_level"
    level.attrs["units"] = "hPa"

    point = grp.create_dataset("point", shape=(shape[1],), dtype="i")
    point[:] = np.arange(shape[1])
    point.attrs["long_name"] = "point_index"
    point.attrs["units"] = "none"

    # Create a temperature dataset with two dimensions in the Data group
    dset = grp.create_dataset("temperature", shape=shape, dtype="f")
    dset.attrs["long_name"] = "air_temperature"
    dset.attrs["units"] = "K"

# Testing
with h5py.File(filename, "r") as f:
    for grp in f:
        print(f[grp].name)
        for dset in f[grp]:
            print(f[f"{grp}/{dset}"])
            print(f[f"{grp}/{dset}"][:])
            for attr_name, attr_value in f[f"{grp}/{dset}"].attrs.items():
                print(f"{attr_name}: {attr_value}")
