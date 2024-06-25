from ..data_loader import BEIRDataLoader
from dataclasses import dataclass

@dataclass
class Robust04QueryInstance:
    id : str
    text : str

@dataclass
class Robust04DocInstance:
    id : str
    text : str

@dataclass
class Robust04QrelInstance:
    qid : str
    did : str
    score : int

class Robust04DataLoader(BEIRDataLoader):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/robust04', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> Robust04QueryInstance:
        return Robust04QueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> Robust04DocInstance:
        return Robust04DocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> Robust04QrelInstance:
        return Robust04QrelInstance(**kwargs)

    def __str__(self) -> str:
        return 'Robust04DataLoader()'

    def __repr__(self) -> str:
        return 'Robust04DataLoader()'
