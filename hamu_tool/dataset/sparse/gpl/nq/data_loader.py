from ..data_loader import GPLDataLoader
from dataclasses import dataclass

@dataclass
class GPLNQQueryInstance:
    id : str
    text : str

@dataclass
class GPLNQDocInstance:
    id : str
    text : str
    title : str

@dataclass
class GPLNQQrelInstance:
    qid : str
    did : str
    score : int

@dataclass
class GPLNQHnegInstance:
    qid : str
    did : str

@dataclass
class GPLNQTripleInstance:
    qid : str
    pos : str
    neg : str
    score : float

class GPLNQDataLoader(GPLDataLoader):
    def __init__(self, *args, **kwargs):
        super().__init__('gpl/nq', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> GPLNQQueryInstance:
        return GPLNQQueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> GPLNQDocInstance:
        return GPLNQDocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> GPLNQQrelInstance:
        return GPLNQQrelInstance(**kwargs)

    def make_hneg_instance(self, **kwargs) -> GPLNQHnegInstance:
        return GPLNQHnegInstance(**kwargs)

    def make_triple_instance(self, **kwargs) -> GPLNQTripleInstance:
        return GPLNQTripleInstance(**kwargs)

    def __str__(self) -> str:
        return 'GPLNQDataLoader()'

    def __repr__(self) -> str:
        return 'GPLNQDataLoader()'
