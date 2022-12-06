from collections.abc import Iterable
import pathlib as pl
from io import open

def build_string(name: str, value):
    return "{} = {}\n".format(name, value)

def call(
    name: str,
    ext: str,
    tags: list,
    fp: str | pl.Path = None,
    **kwargs
    ):
    cfg = open(
        str(pl.Path(__file__).parent) + "/_{}.conf".format(name.lower()) if fp is None else pl.Path(fp),
        "w+", encoding="utf-8"
        )
    cfg.writelines(
        [
            build_string("name", name),
            build_string("ext", ext),
            build_string("tags", tags)
        ] + [build_string(kw, val) for kw, val in kwargs.items()]
    )
