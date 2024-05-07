from .data_loader_base import DataLoaderQDRBase
from dataclasses import dataclass
from typing import Iterator

@dataclass
class FEVERQueryInstance:
    id : str
    text : str

@dataclass
class FEVERDocInstance:
    id : str
    text : str
    title : str

@dataclass
class FEVERQrelInstance:
    qid : str
    did : str
    score : int

class FEVERDataLoader(DataLoaderQDRBase):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/fever', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> FEVERQueryInstance:
        return FEVERQueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> FEVERDocInstance:
        return FEVERDocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> FEVERQrelInstance:
        return FEVERQrelInstance(**kwargs)

    def __str__(self) -> str:
        return 'FEVERDataLoader()'

    def __repr__(self) -> str:
        return 'FEVERDataLoader()'
