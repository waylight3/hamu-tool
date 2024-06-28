from ..data_loader import GPLDataLoader
from dataclasses import dataclass

@dataclass
class GPLQuoraQueryInstance:
    id : str
    text : str

@dataclass
class GPLQuoraDocInstance:
    id : str
    text : str
    title : str

@dataclass
class GPLQuoraQrelInstance:
    qid : str
    did : str
    score : int

@dataclass
class GPLQuoraHnegInstance:
    qid : str
    did : str

@dataclass
class GPLQuoraTripleInstance:
    qid : str
    pos : str
    neg : str
    score : float

class GPLQuoraDataLoader(GPLDataLoader):
    def __init__(self, *args, **kwargs):
        super().__init__('gpl/quora', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> GPLQuoraQueryInstance:
        return GPLQuoraQueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> GPLQuoraDocInstance:
        return GPLQuoraDocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> GPLQuoraQrelInstance:
        return GPLQuoraQrelInstance(**kwargs)

    def make_hneg_instance(self, **kwargs) -> GPLQuoraHnegInstance:
        return GPLQuoraHnegInstance(**kwargs)

    def make_triple_instance(self, **kwargs) -> GPLQuoraTripleInstance:
        return GPLQuoraTripleInstance(**kwargs)

    def __str__(self) -> str:
        return 'GPLQuoraDataLoader()'

    def __repr__(self) -> str:
        return 'GPLQuoraDataLoader()'
