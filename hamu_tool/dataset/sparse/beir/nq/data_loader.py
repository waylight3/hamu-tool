from ..data_loader import BEIRDataLoader
from dataclasses import dataclass

@dataclass
class BEIRNQQueryInstance:
    id : str
    text : str

@dataclass
class BEIRNQDocInstance:
    id : str
    text : str
    title : str

@dataclass
class BEIRNQQrelInstance:
    qid : str
    did : str
    score : int

class BEIRNQDataLoaderader(BEIRDataLoader):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/nq', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> BEIRNQQueryInstance:
        return BEIRNQQueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> BEIRNQDocInstance:
        return BEIRNQDocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> BEIRNQQrelInstance:
        return BEIRNQQrelInstance(**kwargs)

    def __str__(self) -> str:
        return 'BEIRNQDataLoader()'

    def __repr__(self) -> str:
        return 'BEIRNQDataLoader()'
