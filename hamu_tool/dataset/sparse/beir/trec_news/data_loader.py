from ..data_loader import BEIRDataLoader
from dataclasses import dataclass

@dataclass
class TrecNewsQueryInstance:
    id : str
    text : str

@dataclass
class TrecNewsDocInstance:
    id : str
    text : str
    title : str
    url : str
    author : str
    type : str
    source : str
    published_date : int

@dataclass
class TrecNewsQrelInstance:
    qid : str
    did : str
    score : int

class TrecNewsDataLoader(BEIRDataLoader):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/trec-news', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> TrecNewsQueryInstance:
        return TrecNewsQueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> TrecNewsDocInstance:
        return TrecNewsDocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> TrecNewsQrelInstance:
        return TrecNewsQrelInstance(**kwargs)

    def __str__(self) -> str:
        return 'TrecNewsDataLoader()'

    def __repr__(self) -> str:
        return 'TrecNewsDataLoader()'
