from ..data_loader import BEIRDataLoader
from dataclasses import dataclass

@dataclass
class BEIRQuoraQueryInstance:
    id : str
    text : str

@dataclass
class BEIRQuoraDocInstance:
    id : str
    text : str

@dataclass
class BEIRQuoraQrelInstance:
    qid : str
    did : str
    score : int

class BEIRQuoraDataLoader(BEIRDataLoader):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/quora', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> BEIRQuoraQueryInstance:
        return BEIRQuoraQueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> BEIRQuoraDocInstance:
        return BEIRQuoraDocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> BEIRQuoraQrelInstance:
        return BEIRQuoraQrelInstance(**kwargs)

    def __str__(self) -> str:
        return 'BEIRQuoraDataLoader()'

    def __repr__(self) -> str:
        return 'BEIRQuoraDataLoader()'
