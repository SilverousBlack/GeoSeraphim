import pathlib as pl
from io import open

def call(typ: str, loc: str = None):
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
