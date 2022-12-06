# GeoSeraphim

> Angels descend and survey the Earth

A centralized package for interfacing with geographical data.

## GeoSeraphim is in Development!

> The following commands assume that the current working directory is the repository directory; kindly use `cd` to the path of the repository directory.

***WARING: VIRTUAL ENVIRONMENT IS RECOMMENDED*** 

This library relies on `GDAL` and `rasterio` libraries which cannot be directly installed through `pip`.

### Installing `GDAL` and `rasterio` Pre-Requisites

For ease, `GDAL` and `rasterio` can be installed through `conda` or `miniconda`.

If, however using `conda` or `miniconda` is not possible or desired, read the installation guide from `rasterio` found [here](https://rasterio.readthedocs.io/en/latest/installation.html).

### Installing Other Pre-Requisites

After which the other requirements can be installed through `pip` via the command:

* `pip install -U -r requirements.txt`; or
* `py -m pip install -U -r requirements.txt`

### Building and Installing the Library

To build the project and subsequently install the developement versions:

1. Install `build` through `pip` via the command `pip install -U build`.
2. Build the wheels for the project via the command `py -m build`.
3. Wait for the build process to finish.
4. Install the library through `pip` via the command `pip install dist/GeoSeraphim-*VERSION*-py3-none-any.whl`

### Further Reading

#### Configuration Files

Configuration files are automatically generated on the first run of GeoSeraphim; this would contain configurations for the entire system as well as recipe configurations for output files.

Customizing these files shall be made fully possible in future releases.

#### Seraphanda `.seraph` Files

This file output type is the default output type of `GeoSeraphim` and designed to contain and handle all information on a given map. Internally, a Seraphanda file contains all known information on a map in similar to a `ndarray` form, such that it can be easily plotted, rendered and converted to other types.

#### GeoCSV `.gcsv` Files

This file output type is a lightweight, easily readable table of entries of all known points in a map; it is good for retaining data integrity through multiple uses. Internally it similar to a CSV `.csv` file, which means it can be directly read by `pandas` and rendered as a `DataFrame`.
