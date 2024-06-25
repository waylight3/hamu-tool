from ..data_loader import BEIRDataLoader
from dataclasses import dataclass

@dataclass
class NFCorpusQueryInstance:
    id : str
    text : str
    url : str

@dataclass
class NFCorpusDocInstance:
    id : str
    text : str
    title : str
    url : str

@dataclass
class NFCorpusQrelInstance:
    qid : str
    did : str
    score : int

class NFCorpusDataLoader(BEIRDataLoader):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/nfcorpus', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> NFCorpusQueryInstance:
        return NFCorpusQueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> NFCorpusDocInstance:
        return NFCorpusDocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> NFCorpusQrelInstance:
        return NFCorpusQrelInstance(**kwargs)

    def __str__(self) -> str:
        return 'NFCorpusDataLoader()'

    def __repr__(self) -> str:
        return 'NFCorpusDataLoader()'
