from .data_loader_base import DataLoaderQDRBase
from dataclasses import dataclass
from typing import Iterator

@dataclass
class BioASQQueryInstance:
    id : str
    text : str

@dataclass
class BioASQDocInstance:
    id : str
    text : str
    title : str
    journal : str
    year : int
    pmid : str
    mesh_major : list[str]

@dataclass
class BioASQQrelInstance:
    qid : str
    did : str
    score : int

class BioASQDataLoader(DataLoaderQDRBase):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/bioasq', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> BioASQQueryInstance:
        return BioASQQueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> BioASQDocInstance:
        return BioASQDocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> BioASQQrelInstance:
        return BioASQQrelInstance(**kwargs)

    def __str__(self) -> str:
        return 'BioASQDataLoader()'

    def __repr__(self) -> str:
        return 'BioASQDataLoader()'
