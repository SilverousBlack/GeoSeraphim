from collections.abc import Iterable
import pathlib as pl
from io import open

def build_string(name: str, value):
    return "{} = {}\n".format(name, value)

def call(
    targets: list,
    output: str,
    fp: str | pl.Path = None,
    **kwargs
    ):
    cfg = open(
        str(pl.Path(__file__).parent) + "/sys.conf" if fp is None else pl.Path(fp),
        "w+", encoding="utf-8"
        )
    cfg.writelines(
        [
            build_string("targets", targets),
            build_string("output", output)
        ] + [build_string(kw, val) for kw, val in kwargs.items()]
    )
