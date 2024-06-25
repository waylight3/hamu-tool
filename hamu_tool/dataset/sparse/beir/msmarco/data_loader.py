from ..data_loader import BEIRDataLoader
from dataclasses import dataclass

@dataclass
class MSMARCOQueryInstance:
    id : str
    text : str

@dataclass
class MSMARCODocInstance:
    id : str
    text : str

@dataclass
class MSMARCOQrelInstance:
    qid : str
    did : str
    score : int

class MSMARCODataLoader(BEIRDataLoader):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/msmarco', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> MSMARCOQueryInstance:
        return MSMARCOQueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> MSMARCODocInstance:
        return MSMARCODocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> MSMARCOQrelInstance:
        return MSMARCOQrelInstance(**kwargs)

    def __str__(self) -> str:
        return 'MSMARCODataLoader()'

    def __repr__(self) -> str:
        return 'MSMARCODataLoader()'
