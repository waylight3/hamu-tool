from .data_loader_base import DataLoaderQDRBase
from dataclasses import dataclass
from typing import Iterator

@dataclass
class NQQueryInstance:
    id : str
    text : str

@dataclass
class NQDocInstance:
    id : str
    text : str
    title : str

@dataclass
class NQQrelInstance:
    qid : str
    did : str
    score : int

class NQDataLoader(DataLoaderQDRBase):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/nq', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> NQQueryInstance:
        return NQQueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> NQDocInstance:
        return NQDocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> NQQrelInstance:
        return NQQrelInstance(**kwargs)

    def __str__(self) -> str:
        return 'NQDataLoader()'

    def __repr__(self) -> str:
        return 'NQDataLoader()'
