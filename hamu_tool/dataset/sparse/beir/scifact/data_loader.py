from ..data_loader import BEIRDataLoader
from dataclasses import dataclass

@dataclass
class BEIRSciFactQueryInstance:
    id : str
    text : str

@dataclass
class BEIRSciFactDocInstance:
    id : str
    text : str
    title : str

@dataclass
class BEIRSciFactQrelInstance:
    qid : str
    did : str
    score : int

class BEIRSciFactDataLoader(BEIRDataLoader):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/scifact', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> BEIRSciFactQueryInstance:
        return BEIRSciFactQueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> BEIRSciFactDocInstance:
        return BEIRSciFactDocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> BEIRSciFactQrelInstance:
        return BEIRSciFactQrelInstance(**kwargs)

    def __str__(self) -> str:
        return 'BEIRSciFactDataLoader()'

    def __repr__(self) -> str:
        return 'BEIRSciFactDataLoader()'
