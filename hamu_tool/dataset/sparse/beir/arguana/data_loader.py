from ..data_loader import BEIRDataLoader
from dataclasses import dataclass

@dataclass
class BEIRArguanaQueryInstance:
    id : str
    text : str

@dataclass
class BEIRArguanaDocInstance:
    id : str
    text : str
    title : str

@dataclass
class BEIRArguanaQrelInstance:
    qid : str
    did : str
    score : int

class BEIRArguanaDataLoader(BEIRDataLoader):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/arguana', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> BEIRArguanaQueryInstance:
        return BEIRArguanaQueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> BEIRArguanaDocInstance:
        return BEIRArguanaDocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> BEIRArguanaQrelInstance:
        return BEIRArguanaQrelInstance(**kwargs)

    def __str__(self) -> str:
        return 'BEIRArguanaDataLoader()'

    def __repr__(self) -> str:
        return 'BEIRArguanaDataLoader()'
