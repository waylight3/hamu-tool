from ..data_loader import BEIRDataLoader
from dataclasses import dataclass

@dataclass
class BEIRHotpotQAQueryInstance:
    id : str
    text : str

@dataclass
class BEIRHotpotQADocInstance:
    id : str
    text : str
    title : str
    url : str

@dataclass
class BEIRHotpotQAQrelInstance:
    qid : str
    did : str
    score : int

class BEIRHotpotQADataLoader(BEIRDataLoader):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/hotpotqa', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> BEIRHotpotQAQueryInstance:
        return BEIRHotpotQAQueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> BEIRHotpotQADocInstance:
        return BEIRHotpotQADocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> BEIRHotpotQAQrelInstance:
        return BEIRHotpotQAQrelInstance(**kwargs)

    def __str__(self) -> str:
        return 'BEIRHotpotQADataLoader()'

    def __repr__(self) -> str:
        return 'BEIRHotpotQADataLoader()'
