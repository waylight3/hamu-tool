from ..data_loader import GPLDataLoader
from dataclasses import dataclass

@dataclass
class GPLFEVERQueryInstance:
    id : str
    text : str

@dataclass
class GPLFEVERDocInstance:
    id : str
    text : str
    title : str

@dataclass
class GPLFEVERQrelInstance:
    qid : str
    did : str
    score : int

@dataclass
class GPLFEVERHnegInstance:
    qid : str
    did : str

@dataclass
class GPLFEVERTripleInstance:
    qid : str
    pos : str
    neg : str
    score : float

class GPLFEVERDataLoader(GPLDataLoader):
    def __init__(self, *args, **kwargs):
        super().__init__('gpl/fever', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> GPLFEVERQueryInstance:
        return GPLFEVERQueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> GPLFEVERDocInstance:
        return GPLFEVERDocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> GPLFEVERQrelInstance:
        return GPLFEVERQrelInstance(**kwargs)

    def make_hneg_instance(self, **kwargs) -> GPLFEVERHnegInstance:
        return GPLFEVERHnegInstance(**kwargs)

    def make_triple_instance(self, **kwargs) -> GPLFEVERTripleInstance:
        return GPLFEVERTripleInstance(**kwargs)

    def __str__(self) -> str:
        return 'GPLFEVERDataLoader()'

    def __repr__(self) -> str:
        return 'GPLFEVERDataLoader()'
