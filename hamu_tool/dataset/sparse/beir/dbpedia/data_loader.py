from ..data_loader import BEIRDataLoader
from dataclasses import dataclass

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

class DBPediaDataLoader(BEIRDataLoader):
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
