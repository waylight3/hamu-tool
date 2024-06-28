from ..data_loader import GPLDataLoader
from dataclasses import dataclass

@dataclass
class GPLClimateFEVERQueryInstance:
    id : str
    text : str

@dataclass
class GPLClimateFEVERDocInstance:
    id : str
    text : str
    title : str

@dataclass
class GPLClimateFEVERQrelInstance:
    qid : str
    did : str
    score : int

@dataclass
class GPLClimateFEVERHnegInstance:
    qid : str
    did : str

@dataclass
class GPLClimateFEVERTripleInstance:
    qid : str
    pos : str
    neg : str
    score : float

class GPLClimateFEVERDataLoader(GPLDataLoader):
    def __init__(self, *args, **kwargs):
        super().__init__('gpl/climate-fever', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> GPLClimateFEVERQueryInstance:
        return GPLClimateFEVERQueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> GPLClimateFEVERDocInstance:
        return GPLClimateFEVERDocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> GPLClimateFEVERQrelInstance:
        return GPLClimateFEVERQrelInstance(**kwargs)

    def make_hneg_instance(self, **kwargs) -> GPLClimateFEVERHnegInstance:
        return GPLClimateFEVERHnegInstance(**kwargs)

    def make_triple_instance(self, **kwargs) -> GPLClimateFEVERTripleInstance:
        return GPLClimateFEVERTripleInstance(**kwargs)

    def __str__(self) -> str:
        return 'GPLClimateFEVERDataLoader()'

    def __repr__(self) -> str:
        return 'GPLClimateFEVERDataLoader()'
