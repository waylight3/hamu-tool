from ..data_loader import GPLDataLoader
from dataclasses import dataclass

@dataclass
class GPLFiQAQueryInstance:
    id : str
    text : str

@dataclass
class GPLFiQADocInstance:
    id : str
    text : str
    title : str

@dataclass
class GPLFiQAQrelInstance:
    qid : str
    did : str
    score : int

@dataclass
class GPLFiQAHnegInstance:
    qid : str
    did : str

@dataclass
class GPLFiQATripleInstance:
    qid : str
    pos : str
    neg : str
    score : float

class GPLFiQADataLoader(GPLDataLoader):
    def __init__(self, *args, **kwargs):
        super().__init__('gpl/fiqa', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> GPLFiQAQueryInstance:
        return GPLFiQAQueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> GPLFiQADocInstance:
        return GPLFiQADocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> GPLFiQAQrelInstance:
        return GPLFiQAQrelInstance(**kwargs)

    def make_hneg_instance(self, **kwargs) -> GPLFiQAHnegInstance:
        return GPLFiQAHnegInstance(**kwargs)

    def make_triple_instance(self, **kwargs) -> GPLFiQATripleInstance:
        return GPLFiQATripleInstance(**kwargs)

    def __str__(self) -> str:
        return 'GPLFiQADataLoader()'

    def __repr__(self) -> str:
        return 'GPLFiQADataLoader()'
