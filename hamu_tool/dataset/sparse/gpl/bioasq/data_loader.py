from ..data_loader import GPLDataLoader
from dataclasses import dataclass

@dataclass
class GPLBioASQQueryInstance:
    id : str
    text : str

@dataclass
class GPLBioASQDocInstance:
    id : str
    text : str
    title : str

@dataclass
class GPLBioASQQrelInstance:
    qid : str
    did : str
    score : int

@dataclass
class GPLBioASQHnegInstance:
    qid : str
    did : str

@dataclass
class GPLBioASQTripleInstance:
    qid : str
    pos : str
    neg : str
    score : float

class GPLBioASQDataLoader(GPLDataLoader):
    def __init__(self, *args, **kwargs):
        super().__init__('gpl/bioasq', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> GPLBioASQQueryInstance:
        return GPLBioASQQueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> GPLBioASQDocInstance:
        return GPLBioASQDocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> GPLBioASQQrelInstance:
        return GPLBioASQQrelInstance(**kwargs)

    def make_hneg_instance(self, **kwargs) -> GPLBioASQHnegInstance:
        return GPLBioASQHnegInstance(**kwargs)

    def make_triple_instance(self, **kwargs) -> GPLBioASQTripleInstance:
        return GPLBioASQTripleInstance(**kwargs)

    def __str__(self) -> str:
        return 'GPLBioASQDataLoader()'

    def __repr__(self) -> str:
        return 'GPLBioASQDataLoader()'
