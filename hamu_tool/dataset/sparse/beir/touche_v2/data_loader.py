from ..data_loader import BEIRDataLoader
from dataclasses import dataclass

@dataclass
class BEIRTouchev2QueryInstance:
    id : str
    text : str
    description : str
    narrative : str

@dataclass
class BEIRTouchev2DocInstance:
    id : str
    text : str
    title : str
    stance : str
    url : str

@dataclass
class BEIRTouchev2QrelInstance:
    qid : str
    did : str
    score : int

class BEIRTouchev2DataLoader(BEIRDataLoader):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/touche-v2', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> BEIRTouchev2QueryInstance:
        return BEIRTouchev2QueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> BEIRTouchev2DocInstance:
        return BEIRTouchev2DocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> BEIRTouchev2QrelInstance:
        return BEIRTouchev2QrelInstance(**kwargs)

    def __str__(self) -> str:
        return 'BEIRTouchev2DataLoader()'

    def __repr__(self) -> str:
        return 'BEIRTouchev2DataLoader()'
