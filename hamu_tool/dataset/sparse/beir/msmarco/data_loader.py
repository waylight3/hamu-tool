from ..data_loader import BEIRDataLoader
from dataclasses import dataclass

@dataclass
class BEIRMSMARCOQueryInstance:
    id : str
    text : str

@dataclass
class BEIRMSMARCODocInstance:
    id : str
    text : str

@dataclass
class BEIRMSMARCOQrelInstance:
    qid : str
    did : str
    score : int

class BEIRMSMARCODataLoader(BEIRDataLoader):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/msmarco', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> BEIRMSMARCOQueryInstance:
        return BEIRMSMARCOQueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> BEIRMSMARCODocInstance:
        return BEIRMSMARCODocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> BEIRMSMARCOQrelInstance:
        return BEIRMSMARCOQrelInstance(**kwargs)

    def __str__(self) -> str:
        return 'BEIRMSMARCODataLoader()'

    def __repr__(self) -> str:
        return 'BEIRMSMARCODataLoader()'
