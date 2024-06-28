from ..data_loader import GPLDataLoader
from dataclasses import dataclass

@dataclass
class GPLTrecNewsQueryInstance:
    id : str
    text : str

@dataclass
class GPLTrecNewsDocInstance:
    id : str
    text : str
    title : str

@dataclass
class GPLTrecNewsQrelInstance:
    qid : str
    did : str
    score : int

@dataclass
class GPLTrecNewsHnegInstance:
    qid : str
    did : str

@dataclass
class GPLTrecNewsTripleInstance:
    qid : str
    pos : str
    neg : str
    score : float

class GPLTrecNewsDataLoader(GPLDataLoader):
    def __init__(self, *args, **kwargs):
        super().__init__('gpl/trec-news', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> GPLTrecNewsQueryInstance:
        return GPLTrecNewsQueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> GPLTrecNewsDocInstance:
        return GPLTrecNewsDocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> GPLTrecNewsQrelInstance:
        return GPLTrecNewsQrelInstance(**kwargs)

    def make_hneg_instance(self, **kwargs) -> GPLTrecNewsHnegInstance:
        return GPLTrecNewsHnegInstance(**kwargs)

    def make_triple_instance(self, **kwargs) -> GPLTrecNewsTripleInstance:
        return GPLTrecNewsTripleInstance(**kwargs)

    def __str__(self) -> str:
        return 'GPLTrecNewsDataLoader()'

    def __repr__(self) -> str:
        return 'GPLTrecNewsDataLoader()'
