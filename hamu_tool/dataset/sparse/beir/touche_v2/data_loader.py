from ..data_loader import BEIRDataLoader
from dataclasses import dataclass

@dataclass
class Touchev2QueryInstance:
    id : str
    text : str
    description : str
    narrative : str

@dataclass
class Touchev2DocInstance:
    id : str
    text : str
    title : str
    stance : str
    url : str

@dataclass
class Touchev2QrelInstance:
    qid : str
    did : str
    score : int

class Touchev2DataLoader(BEIRDataLoader):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/touche-v2', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> Touchev2QueryInstance:
        return Touchev2QueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> Touchev2DocInstance:
        return Touchev2DocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> Touchev2QrelInstance:
        return Touchev2QrelInstance(**kwargs)

    def __str__(self) -> str:
        return 'Touchev2DataLoader()'

    def __repr__(self) -> str:
        return 'Touchev2DataLoader()'
