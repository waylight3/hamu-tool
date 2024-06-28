from ..data_loader import BEIRDataLoader
from dataclasses import dataclass

@dataclass
class BEIRSignal1MQueryInstance:
    id : str
    text : str

@dataclass
class BEIRSignal1MDocInstance:
    id : str
    text : str

@dataclass
class BEIRSignal1MQrelInstance:
    qid : str
    did : str
    score : int

class BEIRSignal1MDataLoader(BEIRDataLoader):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/signal1m', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> BEIRSignal1MQueryInstance:
        return BEIRSignal1MQueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> BEIRSignal1MDocInstance:
        return BEIRSignal1MDocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> BEIRSignal1MQrelInstance:
        return BEIRSignal1MQrelInstance(**kwargs)

    def __str__(self) -> str:
        return 'BEIRSignal1MDataLoader()'

    def __repr__(self) -> str:
        return 'BEIRSignal1MDataLoader()'
