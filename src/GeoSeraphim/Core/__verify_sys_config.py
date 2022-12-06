import pathlib as pl
from io import open
import typing

def call(conf: dict):
    internal = {}
    for kw, val in conf:
        key = kw.lower()
        if key == "targets":
            buf = []
            for data in val:
                dt: typing.Any
                if data[0] == ".":
                    dt = data[1:-1]
                dt = dt.lower()
                buf.append(dt)
            internal[key] = buf
        if 