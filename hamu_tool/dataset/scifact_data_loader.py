from .data_loader_base import DataLoaderQDRBase
from dataclasses import dataclass
from typing import Iterator

@dataclass
class SciFactQueryInstance:
    id : str
    text : str

@dataclass
class SciFactDocInstance:
    id : str
    text : str
    title : str

@dataclass
class SciFactQrelInstance:
    qid : str
    did : str
    score : int

class SciFactDataLoader(DataLoaderQDRBase):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/scifact', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> SciFactQueryInstance:
        return SciFactQueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> SciFactDocInstance:
        return SciFactDocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> SciFactQrelInstance:
        return SciFactQrelInstance(**kwargs)

    def __str__(self) -> str:
        return 'SciFactDataLoader()'

    def __repr__(self) -> str:
        return 'SciFactDataLoader()'
