from .data_loader_base import DataLoaderQDRBase
from dataclasses import dataclass
from typing import Iterator

@dataclass
class Signal1MQueryInstance:
    id : str
    text : str

@dataclass
class Signal1MDocInstance:
    id : str
    text : str

@dataclass
class Signal1MQrelInstance:
    qid : str
    did : str
    score : int

class Signal1MDataLoader(DataLoaderQDRBase):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/signal1m', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> Signal1MQueryInstance:
        return Signal1MQueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> Signal1MDocInstance:
        return Signal1MDocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> Signal1MQrelInstance:
        return Signal1MQrelInstance(**kwargs)

    def __str__(self) -> str:
        return 'Signal1MDataLoader()'

    def __repr__(self) -> str:
        return 'Signal1MDataLoader()'
