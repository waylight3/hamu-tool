from ..data_loader import BEIRDataLoader
from dataclasses import dataclass

@dataclass
class ArguanaQueryInstance:
    id : str
    text : str

@dataclass
class ArguanaDocInstance:
    id : str
    text : str
    title : str

@dataclass
class ArguanaQrelInstance:
    qid : str
    did : str
    score : int

class ArguanaDataLoader(BEIRDataLoader):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/arguana', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> ArguanaQueryInstance:
        return ArguanaQueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> ArguanaDocInstance:
        return ArguanaDocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> ArguanaQrelInstance:
        return ArguanaQrelInstance(**kwargs)

    def __str__(self) -> str:
        return 'ArguanaDataLoader()'

    def __repr__(self) -> str:
        return 'ArguanaDataLoader()'
