from ..data_loader import GPLDataLoader
from dataclasses import dataclass

@dataclass
class GPLDBPediaQueryInstance:
    id : str
    text : str

@dataclass
class GPLDBPediaDocInstance:
    id : str
    text : str
    title : str

@dataclass
class GPLDBPediaQrelInstance:
    qid : str
    did : str
    score : int

@dataclass
class GPLDBPediaHnegInstance:
    qid : str
    did : str

@dataclass
class GPLDBPediaTripleInstance:
    qid : str
    pos : str
    neg : str
    score : float

class GPLDBPediaDataLoader(GPLDataLoader):
    def __init__(self, *args, **kwargs):
        super().__init__('gpl/dbpedia', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> GPLDBPediaQueryInstance:
        return GPLDBPediaQueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> GPLDBPediaDocInstance:
        return GPLDBPediaDocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> GPLDBPediaQrelInstance:
        return GPLDBPediaQrelInstance(**kwargs)

    def make_hneg_instance(self, **kwargs) -> GPLDBPediaHnegInstance:
        return GPLDBPediaHnegInstance(**kwargs)

    def make_triple_instance(self, **kwargs) -> GPLDBPediaTripleInstance:
        return GPLDBPediaTripleInstance(**kwargs)

    def __str__(self) -> str:
        return 'GPLDBPediaDataLoader()'

    def __repr__(self) -> str:
        return 'GPLDBPediaDataLoader()'
