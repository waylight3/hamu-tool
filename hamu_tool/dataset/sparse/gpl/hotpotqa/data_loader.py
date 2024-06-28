from ..data_loader import GPLDataLoader
from dataclasses import dataclass

@dataclass
class GPLHotpotQAQueryInstance:
    id : str
    text : str

@dataclass
class GPLHotpotQADocInstance:
    id : str
    text : str
    title : str

@dataclass
class GPLHotpotQAQrelInstance:
    qid : str
    did : str
    score : int

@dataclass
class GPLHotpotQAHnegInstance:
    qid : str
    did : str

@dataclass
class GPLHotpotQATripleInstance:
    qid : str
    pos : str
    neg : str
    score : float

class GPLHotpotQADataLoader(GPLDataLoader):
    def __init__(self, *args, **kwargs):
        super().__init__('gpl/hotpotqa', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> GPLHotpotQAQueryInstance:
        return GPLHotpotQAQueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> GPLHotpotQADocInstance:
        return GPLHotpotQADocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> GPLHotpotQAQrelInstance:
        return GPLHotpotQAQrelInstance(**kwargs)

    def make_hneg_instance(self, **kwargs) -> GPLHotpotQAHnegInstance:
        return GPLHotpotQAHnegInstance(**kwargs)

    def make_triple_instance(self, **kwargs) -> GPLHotpotQATripleInstance:
        return GPLHotpotQATripleInstance(**kwargs)

    def __str__(self) -> str:
        return 'GPLHotpotQADataLoader()'

    def __repr__(self) -> str:
        return 'GPLHotpotQADataLoader()'
