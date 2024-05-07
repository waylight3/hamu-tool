from .data_loader_base import DataLoaderQDRBase
from dataclasses import dataclass
from typing import Iterator

@dataclass
class SciDocsQueryInstance:
    id : str
    text : str
    authors : list[str]
    year : int
    cited_by : list[str]
    references : list[str]

@dataclass
class SciDocsDocInstance:
    id : str
    text : str
    title : str
    authors : list[str]
    year : int
    cited_by : list[str]
    references : list[str]

@dataclass
class SciDocsQrelInstance:
    qid : str
    did : str
    score : int

class SciDocsDataLoader(DataLoaderQDRBase):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/scidocs', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> SciDocsQueryInstance:
        return SciDocsQueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> SciDocsDocInstance:
        return SciDocsDocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> SciDocsQrelInstance:
        return SciDocsQrelInstance(**kwargs)

    def __str__(self) -> str:
        return 'SciDocsDataLoader()'

    def __repr__(self) -> str:
        return 'SciDocsDataLoader()'
