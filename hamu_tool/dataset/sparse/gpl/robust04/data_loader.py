from ..data_loader import GPLDataLoader
from dataclasses import dataclass

@dataclass
class GPLRobust04QueryInstance:
    id : str
    text : str

@dataclass
class GPLRobust04DocInstance:
    id : str
    text : str

@dataclass
class GPLRobust04QrelInstance:
    qid : str
    did : str
    score : int

@dataclass
class GPLRobust04HnegInstance:
    qid : str
    did : str

@dataclass
class GPLRobust04TripleInstance:
    qid : str
    pos : str
    neg : str
    score : float

class GPLRobust04DataLoader(GPLDataLoader):
    def __init__(self, *args, **kwargs):
        super().__init__('gpl/robust04', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> GPLRobust04QueryInstance:
        return GPLRobust04QueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> GPLRobust04DocInstance:
        return GPLRobust04DocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> GPLRobust04QrelInstance:
        return GPLRobust04QrelInstance(**kwargs)

    def make_hneg_instance(self, **kwargs) -> GPLRobust04HnegInstance:
        return GPLRobust04HnegInstance(**kwargs)

    def make_triple_instance(self, **kwargs) -> GPLRobust04TripleInstance:
        return GPLRobust04TripleInstance(**kwargs)

    def __str__(self) -> str:
        return 'GPLRobust04DataLoader()'

    def __repr__(self) -> str:
        return 'GPLRobust04DataLoader()'
