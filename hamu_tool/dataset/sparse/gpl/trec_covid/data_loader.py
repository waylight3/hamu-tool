from ..data_loader import GPLDataLoader
from dataclasses import dataclass

@dataclass
class GPLTrecCovidQueryInstance:
    id : str
    text : str

@dataclass
class GPLTrecCovidDocInstance:
    id : str
    text : str
    title : str

@dataclass
class GPLTrecCovidQrelInstance:
    qid : str
    did : str
    score : int

@dataclass
class GPLTrecCovidHnegInstance:
    qid : str
    did : str

@dataclass
class GPLTrecCovidTripleInstance:
    qid : str
    pos : str
    neg : str
    score : float

class GPLTrecCovidDataLoader(GPLDataLoader):
    def __init__(self, *args, **kwargs):
        super().__init__('gpl/trec-covid', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> GPLTrecCovidQueryInstance:
        return GPLTrecCovidQueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> GPLTrecCovidDocInstance:
        return GPLTrecCovidDocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> GPLTrecCovidQrelInstance:
        return GPLTrecCovidQrelInstance(**kwargs)

    def make_hneg_instance(self, **kwargs) -> GPLTrecCovidHnegInstance:
        return GPLTrecCovidHnegInstance(**kwargs)

    def make_triple_instance(self, **kwargs) -> GPLTrecCovidTripleInstance:
        return GPLTrecCovidTripleInstance(**kwargs)

    def __str__(self) -> str:
        return 'GPLTrecCovidDataLoader()'

    def __repr__(self) -> str:
        return 'GPLTrecCovidDataLoader()'
