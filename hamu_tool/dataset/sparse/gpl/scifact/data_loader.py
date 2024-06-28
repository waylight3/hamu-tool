from ..data_loader import GPLDataLoader
from dataclasses import dataclass

@dataclass
class GPLSciFactQueryInstance:
    id : str
    text : str

@dataclass
class GPLSciFactDocInstance:
    id : str
    text : str
    title : str

@dataclass
class GPLSciFactQrelInstance:
    qid : str
    did : str
    score : int

@dataclass
class GPLSciFactHnegInstance:
    qid : str
    did : str

@dataclass
class GPLSciFactTripleInstance:
    qid : str
    pos : str
    neg : str
    score : float

class GPLSciFactDataLoader(GPLDataLoader):
    def __init__(self, *args, **kwargs):
        super().__init__('gpl/scifact', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> GPLSciFactQueryInstance:
        return GPLSciFactQueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> GPLSciFactDocInstance:
        return GPLSciFactDocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> GPLSciFactQrelInstance:
        return GPLSciFactQrelInstance(**kwargs)

    def make_hneg_instance(self, **kwargs) -> GPLSciFactHnegInstance:
        return GPLSciFactHnegInstance(**kwargs)

    def make_triple_instance(self, **kwargs) -> GPLSciFactTripleInstance:
        return GPLSciFactTripleInstance(**kwargs)

    def __str__(self) -> str:
        return 'GPLSciFactDataLoader()'

    def __repr__(self) -> str:
        return 'GPLSciFactDataLoader()'
