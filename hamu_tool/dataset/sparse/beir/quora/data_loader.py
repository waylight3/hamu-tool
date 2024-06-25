from ..data_loader import BEIRDataLoader
from dataclasses import dataclass

@dataclass
class QuoraQueryInstance:
    id : str
    text : str

@dataclass
class QuoraDocInstance:
    id : str
    text : str

@dataclass
class QuoraQrelInstance:
    qid : str
    did : str
    score : int

class QuoraDataLoader(BEIRDataLoader):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/quora', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> QuoraQueryInstance:
        return QuoraQueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> QuoraDocInstance:
        return QuoraDocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> QuoraQrelInstance:
        return QuoraQrelInstance(**kwargs)

    def __str__(self) -> str:
        return 'QuoraDataLoader()'

    def __repr__(self) -> str:
        return 'QuoraDataLoader()'
