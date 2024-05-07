from .data_loader_base import DataLoaderQDRBase
from dataclasses import dataclass
from typing import Iterator

@dataclass
class DBPediaQueryInstance:
    id : str
    text : str

@dataclass
class DBPediaDocInstance:
    id : str
    text : str
    title : str
    url : str

@dataclass
class DBPediaQrelInstance:
    qid : str
    did : str
    score : int

class DBPediaDataLoader(DataLoaderQDRBase):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/dbpedia', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> DBPediaQueryInstance:
        return DBPediaQueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> DBPediaDocInstance:
        return DBPediaDocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> DBPediaQrelInstance:
        return DBPediaQrelInstance(**kwargs)

    def __str__(self) -> str:
        return 'DBPediaDataLoader()'

    def __repr__(self) -> str:
        return 'DBPediaDataLoader()'
