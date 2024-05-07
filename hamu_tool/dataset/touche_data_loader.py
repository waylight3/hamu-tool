from .data_loader_base import DataLoaderQDRBase
from dataclasses import dataclass
from typing import Iterator

@dataclass
class ToucheQueryInstance:
    id : str
    text : str
    description : str
    narrative : str

@dataclass
class ToucheDocInstance:
    id : str
    text : str
    title : str
    stance : str
    url : str

@dataclass
class ToucheQrelInstance:
    qid : str
    did : str
    score : int

class ToucheDataLoader(DataLoaderQDRBase):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/touche', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> ToucheQueryInstance:
        return ToucheQueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> ToucheDocInstance:
        return ToucheDocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> ToucheQrelInstance:
        return ToucheQrelInstance(**kwargs)

    def __str__(self) -> str:
        return 'ToucheDataLoader()'

    def __repr__(self) -> str:
        return 'ToucheDataLoader()'
