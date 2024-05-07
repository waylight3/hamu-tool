from .data_loader_base import DataLoaderQDRBase
from dataclasses import dataclass
from typing import Iterator

@dataclass
class TrecCovidQueryInstance:
    id : str
    text : str
    narrative : str

@dataclass
class TrecCovidDocInstance:
    id : str
    text : str
    title : str
    url : str
    pubmed_id : str

@dataclass
class TrecCovidQrelInstance:
    qid : str
    did : str
    score : int

class TrecCovidDataLoader(DataLoaderQDRBase):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/trec-covid', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> TrecCovidQueryInstance:
        return TrecCovidQueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> TrecCovidDocInstance:
        return TrecCovidDocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> TrecCovidQrelInstance:
        return TrecCovidQrelInstance(**kwargs)

    def __str__(self) -> str:
        return 'TrecCovidDataLoader()'

    def __repr__(self) -> str:
        return 'TrecCovidDataLoader()'
