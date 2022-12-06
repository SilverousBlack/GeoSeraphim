import pathlib as pl
from io import open

from GeoSeraphim.Core.__load_config import __DATABASE__ as SYSDB
from GeoSeraphim.Core.__edit_type_conf import call as MakeTypeConfig

def build_string(name: str, value):
    return "{} = {}\n".format(name, value)

def call(
    targets: list = None,
    output: list = None,
    fp: str | pl.Path = None,
    **kwargs
    ):
    global SYSDB
    SYSDB.SYSTEM_CONFIGURATION["targets"] = targets if targets is not None else SYSDB.SYSTEM_CONFIGURATION["targets"]
    SYSDB.SYSTEM_CONFIGURATION["output"] = output if output is not None else SYSDB.SYSTEM_CONFIGURATION["output"]
    for kw, val in kwargs.items():
        if kw == "root" and (kw[-1] != "/" or kw[-1] != "\\"):
            SYSDB.SYSTEM_CONFIGURATION[kw + "/"] = val
        else:
            SYSDB.SYSTEM_CONFIGURATION[kw] = val
    cfg = open(
        str(pl.Path(__file__).parent) + "/sys.conf" if fp is None else pl.Path(fp),
        "w+", encoding="utf-8"
        )
    cfg.writelines(
        [
            build_string(kw, val) for kw, val in SYSDB.SYSTEM_CONFIGURATION.items()
        ]
    )
    if "root" in kwargs.keys:
        if not pl.Path(str(pl.Path(SYSDB.SYSTEM_CONFIGURATION["root"])) + "_seraphanda.conf").exists():
            MakeTypeConfig(
                name="Seraphanda",
                ext="seraph",
                tags=[ {"eid": "object"}, {"xpos": "int64"}, {"ypos": "int64"}, {"zpos": "int64"}, "..." ]
            )
        if not pl.Path(str(pl.Path(SYSDB.SYSTEM_CONFIGURATION["root"])) + "_seraphanda.conf").exists():
            MakeTypeConfig(
                name="GeoCSV",
                ext="gcsv",
                tags=[ {"eid": "object"}, {"xpos": "int64"}, {"ypos": "int64"}, {"zpos": "int64"}, "..." ]
            )
        