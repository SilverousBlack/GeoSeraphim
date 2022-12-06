import pathlib as pl
from io import open

class __data:
    SYSTEM_CONFIGURATION: dict
    OUTPUT_CONFIGURATION: dict
    def __init__(self):
        self.SYSTEM_CONFIGURATION = {
            "targets": [],
            "output": ""
        }
        self.OUTPUT_CONFIGURATION = {
            "name": "",
            "ext": "",
            "tags": []
        }
    pass

__DATABASE__ = __data()
__DATABASE__.SYSTEM_CONFIGURATION = {}
__DATABASE__.OUTPUT_CONFIGURATION = {}

def ReadSys(fp: str | pl.Path = None):
    conf = {}
    cfg = open(
        str(pl.Path(__file__).parent) + "/sys.conf" if fp is None else pl.Path(fp),
        "r", encoding="utf-8"
        )
    data = cfg.readlines()
    data = [x.split("=") for x in data]
    for chunk in data:
        buf: str | list
        if chunk[0].strip().lower() == "targets":
            buf = chunk[1].strip()[1:-1]
            buf = buf.split(",")
            buf = [x.strip() for x in buf]
        else:
            buf = chunk[1].strip().lower()
        conf[chunk[0].strip().lower()] = buf
    return conf

def ReadType(typ: str, loc: str = None):
    loc = (str(pl.Path(__file__).parent) if loc is None else loc) 
    loc = loc + "/" if loc[-1] != "/" else loc
    fp = "_{}.conf".format(typ)
    conf = {}
    cfg = open(loc + fp, "r", encoding="utf-8")
    data = cfg.readlines()
    data = [x.split("=") for x in data]
    for chunk in data:
        buf: str | list
        if chunk[0].strip().lower() == "tags":
            buf = chunk[1].strip()[1:-1]
            buf = buf.split(",")
            buf = [x.strip() for x in buf]
        else:
            buf = chunk[1].strip().lower()
        conf[chunk[0].strip().lower()] = buf
    conf["heads"] = {}
    for chunk in conf["tags"]:
        if chunk[0] == "{":
            buf = chunk.strip()[1:-1].split(":")
            conf["heads"][buf[0].strip()] = buf[1].strip()
    return conf

def call(fp: str | pl.Path = None):
    global __DATABASE__
    import sys
    __DATABASE__.SYSTEM_CONFIGURATION = ReadSys(fp)
    __DATABASE__.OUTPUT_CONFIGURATION = ReadType(
        __DATABASE__.SYSTEM_CONFIGURATION["output"], 
        __DATABASE__.SYSTEM_CONFIGURATION["root"] 
        if "root" in __DATABASE__.SYSTEM_CONFIGURATION.keys() 
        else None)
    