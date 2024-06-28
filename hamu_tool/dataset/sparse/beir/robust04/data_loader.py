from ..data_loader import BEIRDataLoader
from dataclasses import dataclass

@dataclass
class BEIRRobust04QueryInstance:
    id : str
    text : str

@dataclass
class BEIRRobust04DocInstance:
    id : str
    text : str

@dataclass
class BEIRRobust04QrelInstance:
    qid : str
    did : str
    score : int

class BEIRRobust04DataLoader(BEIRDataLoader):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/robust04', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> BEIRRobust04QueryInstance:
        return BEIRRobust04QueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> BEIRRobust04DocInstance:
        return BEIRRobust04DocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> BEIRRobust04QrelInstance:
        return BEIRRobust04QrelInstance(**kwargs)

    def __str__(self) -> str:
        return 'BEIRRobust04DataLoader()'

    def __repr__(self) -> str:
        return 'BEIRRobust04DataLoader()'
