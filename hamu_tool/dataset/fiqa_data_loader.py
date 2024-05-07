from .data_loader_base import DataLoaderQDRBase
from dataclasses import dataclass
from typing import Iterator

@dataclass
class FiQAQueryInstance:
    id : str
    text : str

@dataclass
class FiQADocInstance:
    id : str
    text : str

@dataclass
class FiQAQrelInstance:
    qid : str
    did : str
    score : int

class FiQADataLoader(DataLoaderQDRBase):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/fiqa', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> FiQAQueryInstance:
        return FiQAQueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> FiQADocInstance:
        return FiQADocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> FiQAQrelInstance:
        return FiQAQrelInstance(**kwargs)

    def __str__(self) -> str:
        return 'FiQADataLoader()'

    def __repr__(self) -> str:
        return 'FiQADataLoader()'
