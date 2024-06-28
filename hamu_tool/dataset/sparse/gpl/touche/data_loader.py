from ..data_loader import GPLDataLoader
from dataclasses import dataclass

@dataclass
class GPLToucheQueryInstance:
    id : str
    text : str

@dataclass
class GPLToucheDocInstance:
    id : str
    text : str
    title : str

@dataclass
class GPLToucheQrelInstance:
    qid : str
    did : str
    score : int

@dataclass
class GPLToucheHnegInstance:
    qid : str
    did : str

@dataclass
class GPLToucheTripleInstance:
    qid : str
    pos : str
    neg : str
    score : float

class GPLToucheDataLoader(GPLDataLoader):
    def __init__(self, *args, **kwargs):
        super().__init__('gpl/touche', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> GPLToucheQueryInstance:
        return GPLToucheQueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> GPLToucheDocInstance:
        return GPLToucheDocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> GPLToucheQrelInstance:
        return GPLToucheQrelInstance(**kwargs)

    def make_hneg_instance(self, **kwargs) -> GPLToucheHnegInstance:
        return GPLToucheHnegInstance(**kwargs)

    def make_triple_instance(self, **kwargs) -> GPLToucheTripleInstance:
        return GPLToucheTripleInstance(**kwargs)

    def __str__(self) -> str:
        return 'GPLToucheDataLoader()'

    def __repr__(self) -> str:
        return 'GPLToucheDataLoader()'
