from ..data_loader import BEIRDataLoader
from dataclasses import dataclass

@dataclass
class BEIRClimateFEVERQueryInstance:
    id : str
    text : str

@dataclass
class BEIRClimateFEVERDocInstance:
    id : str
    text : str
    title : str

@dataclass
class BEIRClimateFEVERQrelInstance:
    qid : str
    did : str
    score : int

class BEIRClimateFEVERDataLoader(BEIRDataLoader):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/climate-fever', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> BEIRClimateFEVERQueryInstance:
        return BEIRClimateFEVERQueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> BEIRClimateFEVERDocInstance:
        return BEIRClimateFEVERDocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> BEIRClimateFEVERQrelInstance:
        return BEIRClimateFEVERQrelInstance(**kwargs)

    def __str__(self) -> str:
        return 'BEIRClimateFEVERDataLoader()'

    def __repr__(self) -> str:
        return 'BEIRClimateFEVERDataLoader()'
