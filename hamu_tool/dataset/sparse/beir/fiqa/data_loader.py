from ..data_loader import BEIRDataLoader
from dataclasses import dataclass

@dataclass
class BEIRFiQAQueryInstance:
    id : str
    text : str

@dataclass
class BEIRFiQADocInstance:
    id : str
    text : str

@dataclass
class BEIRFiQAQrelInstance:
    qid : str
    did : str
    score : int

class BEIRFiQADataLoader(BEIRDataLoader):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/fiqa', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> BEIRFiQAQueryInstance:
        return BEIRFiQAQueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> BEIRFiQADocInstance:
        return BEIRFiQADocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> BEIRFiQAQrelInstance:
        return BEIRFiQAQrelInstance(**kwargs)

    def __str__(self) -> str:
        return 'BEIRFiQADataLoader()'

    def __repr__(self) -> str:
        return 'BEIRFiQADataLoader()'
