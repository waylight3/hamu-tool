from ..data_loader import GPLDataLoader
from dataclasses import dataclass

@dataclass
class GPLArguanaQueryInstance:
    id : str
    text : str

@dataclass
class GPLArguanaDocInstance:
    id : str
    text : str
    title : str

@dataclass
class GPLArguanaQrelInstance:
    qid : str
    did : str
    score : int

@dataclass
class GPLArguanaHnegInstance:
    qid : str
    did : str

@dataclass
class GPLArguanaTripleInstance:
    qid : str
    pos : str
    neg : str
    score : float

class GPLArguanaDataLoader(GPLDataLoader):
    def __init__(self, *args, **kwargs):
        super().__init__('gpl/arguana', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> GPLArguanaQueryInstance:
        return GPLArguanaQueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> GPLArguanaDocInstance:
        return GPLArguanaDocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> GPLArguanaQrelInstance:
        return GPLArguanaQrelInstance(**kwargs)

    def make_hneg_instance(self, **kwargs) -> GPLArguanaHnegInstance:
        return GPLArguanaHnegInstance(**kwargs)

    def make_triple_instance(self, **kwargs) -> GPLArguanaTripleInstance:
        return GPLArguanaTripleInstance(**kwargs)

    def __str__(self) -> str:
        return 'GPLArguanaDataLoader()'

    def __repr__(self) -> str:
        return 'GPLArguanaDataLoader()'
