from ..data_loader import GPLDataLoader
from dataclasses import dataclass

@dataclass
class GPLSciDocsQueryInstance:
    id : str
    text : str

@dataclass
class GPLSciDocsDocInstance:
    id : str
    text : str
    title : str

@dataclass
class GPLSciDocsQrelInstance:
    qid : str
    did : str
    score : int

@dataclass
class GPLSciDocsHnegInstance:
    qid : str
    did : str

@dataclass
class GPLSciDocsTripleInstance:
    qid : str
    pos : str
    neg : str
    score : float

class GPLSciDocsDataLoader(GPLDataLoader):
    def __init__(self, *args, **kwargs):
        super().__init__('gpl/scidocs', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> GPLSciDocsQueryInstance:
        return GPLSciDocsQueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> GPLSciDocsDocInstance:
        return GPLSciDocsDocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> GPLSciDocsQrelInstance:
        return GPLSciDocsQrelInstance(**kwargs)

    def make_hneg_instance(self, **kwargs) -> GPLSciDocsHnegInstance:
        return GPLSciDocsHnegInstance(**kwargs)

    def make_triple_instance(self, **kwargs) -> GPLSciDocsTripleInstance:
        return GPLSciDocsTripleInstance(**kwargs)

    def __str__(self) -> str:
        return 'GPLSciDocsDataLoader()'

    def __repr__(self) -> str:
        return 'GPLSciDocsDataLoader()'
