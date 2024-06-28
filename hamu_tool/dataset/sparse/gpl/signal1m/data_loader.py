from ..data_loader import GPLDataLoader
from dataclasses import dataclass

@dataclass
class GPLSignal1MQueryInstance:
    id : str
    text : str

@dataclass
class GPLSignal1MDocInstance:
    id : str
    text : str

@dataclass
class GPLSignal1MQrelInstance:
    qid : str
    did : str
    score : int

@dataclass
class GPLSignal1MHnegInstance:
    qid : str
    did : str

@dataclass
class GPLSignal1MTripleInstance:
    qid : str
    pos : str
    neg : str
    score : float

class GPLSignal1MDataLoader(GPLDataLoader):
    def __init__(self, *args, **kwargs):
        super().__init__('gpl/signal1m', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> GPLSignal1MQueryInstance:
        return GPLSignal1MQueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> GPLSignal1MDocInstance:
        return GPLSignal1MDocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> GPLSignal1MQrelInstance:
        return GPLSignal1MQrelInstance(**kwargs)

    def make_hneg_instance(self, **kwargs) -> GPLSignal1MHnegInstance:
        return GPLSignal1MHnegInstance(**kwargs)

    def make_triple_instance(self, **kwargs) -> GPLSignal1MTripleInstance:
        return GPLSignal1MTripleInstance(**kwargs)

    def __str__(self) -> str:
        return 'GPLSignal1MDataLoader()'

    def __repr__(self) -> str:
        return 'GPLSignal1MDataLoader()'
