from ..data_loader import BEIRDataLoader
from dataclasses import dataclass

@dataclass
class BEIRTrecNewsQueryInstance:
    id : str
    text : str

@dataclass
class BEIRTrecNewsDocInstance:
    id : str
    text : str
    title : str
    url : str
    author : str
    type : str
    source : str
    published_date : int

@dataclass
class BEIRTrecNewsQrelInstance:
    qid : str
    did : str
    score : int

class BEIRTrecNewsDataLoader(BEIRDataLoader):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/trec-news', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> BEIRTrecNewsQueryInstance:
        return BEIRTrecNewsQueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> BEIRTrecNewsDocInstance:
        return BEIRTrecNewsDocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> BEIRTrecNewsQrelInstance:
        return BEIRTrecNewsQrelInstance(**kwargs)

    def __str__(self) -> str:
        return 'BEIRTrecNewsDataLoader()'

    def __repr__(self) -> str:
        return 'BEIRTrecNewsDataLoader()'
