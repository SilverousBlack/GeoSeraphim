import pathlib as pl
import typing
import sys

from GeoSeraphim.Core.__make_type_conf import call as MakeTypeConfig

def call(conf: dict):
    internal = {}
    for kw, val in conf.items():
        key = kw.lower()
        if key == "targets":
            buf = []
            for data in val:
                dt: typing.Any
                if data[0] == ".":
                    dt = data[1:-1]
                else:
                    dt = data
                dt = dt.lower()
                buf.append(dt)
            internal[key] = buf
        elif key == "output" and val not in ["seraphanda", "geocsv"]:
            print("Unknown output file definition [{}]; switching to default [seraphanda]".format(val), file=sys.stderr)
            internal[key] = "seraphanda"
        elif key == "root":
            val = val if val[-1] in ["/", "\\"] else val + "/"
            val = pl.Path(val).absolute()
            if not val.exists():
                val.mkdir()
            internal[key] = str(val)
            if not pl.Path(str(val) + "_seraphanda.conf").exists():
                MakeTypeConfig(
                    name="Seraphanda",
                    ext="seraph",
                    tags=[ {"eid": "object"}, {"xpos": "int64"}, {"ypos": "int64"}, {"zpos": "int64"}, "..." ]
                    )
            if not pl.Path(str(val) + "_geocsv.conf").exists():
                MakeTypeConfig(
                    name="GeoCSV",
                    ext="gcsv",
                    tags=[ {"eid": "object"}, {"xpos": "int64"}, {"ypos": "int64"}, {"zpos": "int64"}, "..." ]
                )
        else:
            internal[key] = val
    if "targets" not in conf.keys():
        raise RuntimeError("No target extension type found in system configuration dictionary provided.")
    if "output" not in conf.keys():
        raise RuntimeError("No output file definition found in system configuration dictionary provided.")
    return internal
