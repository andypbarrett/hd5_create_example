"""An example script to create a multi-dimensional HDF5 file"""

import h5py

filename = "test.h5"
shape = (5, 10)
dims = ["level", "point"]

with h5py.File(filename, "w") as f:
    grp = f.create_group("Data")

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
            print(f[f"{grp}/{dset}"][:,:])
            for attr_name, attr_value in f[f"{grp}/{dset}"].attrs.items():
                print(f"{attr_name}: {attr_value}")
