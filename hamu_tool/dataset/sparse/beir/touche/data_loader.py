from ..data_loader import BEIRDataLoader
from dataclasses import dataclass

@dataclass
class BEIRToucheQueryInstance:
    id : str
    text : str
    description : str
    narrative : str

@dataclass
class BEIRToucheDocInstance:
    id : str
    text : str
    title : str
    stance : str
    url : str

@dataclass
class BEIRToucheQrelInstance:
    qid : str
    did : str
    score : int

class BEIRToucheDataLoader(BEIRDataLoader):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/touche', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> BEIRToucheQueryInstance:
        return BEIRToucheQueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> BEIRToucheDocInstance:
        return BEIRToucheDocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> BEIRToucheQrelInstance:
        return BEIRToucheQrelInstance(**kwargs)

    def __str__(self) -> str:
        return 'BEIRToucheDataLoader()'

    def __repr__(self) -> str:
        return 'BEIRToucheDataLoader()'
