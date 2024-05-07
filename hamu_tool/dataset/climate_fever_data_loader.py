from .data_loader_base import DataLoaderQDRBase
from dataclasses import dataclass
from typing import Iterator

@dataclass
class ClimateFEVERQueryInstance:
    id : str
    text : str

@dataclass
class ClimateFEVERDocInstance:
    id : str
    text : str
    title : str

@dataclass
class ClimateFEVERQrelInstance:
    qid : str
    did : str
    score : int

class ClimateFEVERDataLoader(DataLoaderQDRBase):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/climate-fever', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> ClimateFEVERQueryInstance:
        return ClimateFEVERQueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> ClimateFEVERDocInstance:
        return ClimateFEVERDocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> ClimateFEVERQrelInstance:
        return ClimateFEVERQrelInstance(**kwargs)

    def __str__(self) -> str:
        return 'ClimateFEVERDataLoader()'

    def __repr__(self) -> str:
        return 'ClimateFEVERDataLoader()'
