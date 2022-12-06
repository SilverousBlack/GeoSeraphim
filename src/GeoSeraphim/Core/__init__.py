# Pre Requisite Modules and Libraries

## Math and Matrices

import numpy as np
import pandas as pd

## Geographical Libraries

import osgeo
import rasterio as rio

## Plotting

import matplotlib.pyplot as plt
import seaborn as sns

## File System

import pathlib as pl
from io import open

## System Imports

from GeoSeraphim.Core.__load_config import call as LoadConfig, __DATABASE__ as SYSDB
from GeoSeraphim.Core.__read_sys_conf import call as ReadSysConfig
from GeoSeraphim.Core.__read_type_conf import call as ReadTypeConfig
from GeoSeraphim.Core.__edit_sys_conf import call as EditSysConfig
from GeoSeraphim.Core.__edit_type_conf import call as EditTypeConfig
from GeoSeraphim.Core.__make_sys_conf import call as MakeSysConfig
from GeoSeraphim.Core.__make_type_conf import call as MakeTypeConfig

import sys

if not pl.Path(str(pl.Path(__file__).parent) + "/sys.conf").exists():
    print("GeoSeraphim: No Default System Config Found.", file=sys.stderr)
    print("GeoSeraphim: Generating Default System Config.", file=sys.stderr)
    MakeSysConfig(
        ["las", "tif", "geotif", "seraph", "gcsv"],
        "seraphanda"
        )
if not pl.Path(str(pl.Path(__file__).parent if "root" not in SYSDB.SYSTEM_CONFIGURATION.keys() else SYSDB.SYSTEM_CONFIGURATION["root"]) + "/_seraphanda.conf").exists():
    print("GeoSeraphim: No Default Output Type [Serarphanda] Config Found", file=sys.stderr)
    print("GeoSeraphim: Generating Output Type [Serarphanda] Config Found", file=sys.stderr)
    MakeTypeConfig(
        name="Seraphanda",
        ext="seraph",
        tags=[ {"eid": "object"}, {"xpos": "int64"}, {"ypos": "int64"}, {"zpos": "int64"}, "..." ]
        )
if not pl.Path(str(pl.Path(__file__).parent if "root" not in SYSDB.SYSTEM_CONFIGURATION.keys() else SYSDB.SYSTEM_CONFIGURATION["root"]) + "/_seraphanda.conf").exists():
    print("GeoSeraphim: No Default Output Type [GeoCSV] Config Found", file=sys.stderr)
    print("GeoSeraphim: Generating Output Type [GeoCSV] Config Found", file=sys.stderr)
    MakeTypeConfig(
        name="GeoCSV",
        ext="gcsv",
        tags=[ {"eid": "object"}, {"xpos": "int64"}, {"ypos": "int64"}, {"zpos": "int64"}, "..." ]
    )

LoadConfig()
