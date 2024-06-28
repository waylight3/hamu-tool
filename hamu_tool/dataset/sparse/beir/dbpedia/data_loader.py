from ..data_loader import BEIRDataLoader
from dataclasses import dataclass

@dataclass
class BEIRDBPediaQueryInstance:
    id : str
    text : str

@dataclass
class BEIRDBPediaDocInstance:
    id : str
    text : str
    title : str
    url : str

@dataclass
class BEIRDBPediaQrelInstance:
    qid : str
    did : str
    score : int

class BEIRDBPediaDataLoader(BEIRDataLoader):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/dbpedia', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> BEIRDBPediaQueryInstance:
        return BEIRDBPediaQueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> BEIRDBPediaDocInstance:
        return BEIRDBPediaDocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> BEIRDBPediaQrelInstance:
        return BEIRDBPediaQrelInstance(**kwargs)

    def __str__(self) -> str:
        return 'BEIRDBPediaDataLoader()'

    def __repr__(self) -> str:
        return 'BEIRDBPediaDataLoader()'
