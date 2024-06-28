from ..data_loader import BEIRDataLoader
from dataclasses import dataclass

@dataclass
class BEIRFEVERQueryInstance:
    id : str
    text : str

@dataclass
class BEIRFEVERDocInstance:
    id : str
    text : str
    title : str

@dataclass
class BEIRFEVERQrelInstance:
    qid : str
    did : str
    score : int

class BEIRFEVERDataLoader(BEIRDataLoader):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/fever', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> BEIRFEVERQueryInstance:
        return BEIRFEVERQueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> BEIRFEVERDocInstance:
        return BEIRFEVERDocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> BEIRFEVERQrelInstance:
        return BEIRFEVERQrelInstance(**kwargs)

    def __str__(self) -> str:
        return 'BEIRFEVERDataLoader()'

    def __repr__(self) -> str:
        return 'BEIRFEVERDataLoader()'
