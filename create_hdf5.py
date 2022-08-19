"""An example script to create a multi-dimensional HDF5 file"""

import numpy as np
import h5py
import xarray as xr


filename = "test.h5"
npoint = 10
nlevel = 5


# Create a file with one group and two datasets
with h5py.File(filename, "w") as f:
    grp = f.create_group("Data")

    # Create dimension variables
    level = grp.create_dataset("level", shape=(nlevel,), dtype="f")
    level[:] = [1000., 925., 850., 700., 500.]
    level.attrs["long_name"] = "pressure_level"
    level.attrs["units"] = "hPa"
    level.make_scale("level")

    point = grp.create_dataset("point", shape=(npoint,), dtype="i")
    point[:] = np.arange(npoint)
    point.attrs["long_name"] = "point_index"
    point.attrs["units"] = "none"
    point.make_scale("point")

    # Create a temperature dataset with two dimensions in the Data group
    tair = grp.create_dataset("temperature", shape=(nlevel, npoint), dtype="f")
    tair.attrs["long_name"] = "air_temperature"
    tair.attrs["units"] = "K"
    tair.dims[0].attach_scale(level)
    tair.dims[1].attach_scale(point)
    tair.dims[0].label = "level"
    tair.dims[1].label = "point"

    # Create a precipitation dataset with dimension points
    prcp = grp.create_dataset("precipitation", shape=(npoint,), dtype="f")
    prcp.attrs["long_name"] = "precipitation"
    prcp.attrs["units"] = "kg m**-2"
    prcp.dims[0].attach_scale(point)
    prcp.dims[0].label = "point"

    # Add data
    # Adds temperature data by level
    for lev in np.arange(nlevel):
        tair[lev, :] = np.arange(npoint) + (lev*10)
    # Adds precip
    prcp[:] = np.arange(prcp[:].size)

# Test read using h5py
with h5py.File(filename, "r") as f:
    for grp in f:
        print(f[grp].name)
        for dset in f[grp]:
            print(f[f"{grp}/{dset}"])
            print(f[f"{grp}/{dset}"][:])
            for attr_name, attr_value in f[f"{grp}/{dset}"].attrs.items():
                print(f"{attr_name}: {attr_value}")
print("")

# Test read using xarray
with xr.open_dataset(filename, group="/Data") as ds:
    print(ds)
    print(ds.temperature)
    print(ds.precipitation)