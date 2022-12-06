import pathlib as pl
from io import open

from GeoSeraphim.Core.__verify_sys_config import call as VerifySysConfig

def call(fp: str | pl.Path = None):
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
    return VerifySysConfig(conf)
    