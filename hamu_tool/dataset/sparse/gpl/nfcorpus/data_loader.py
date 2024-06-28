from ..data_loader import GPLDataLoader
from dataclasses import dataclass

@dataclass
class GPLNFCorpusQueryInstance:
    id : str
    text : str

@dataclass
class GPLNFCorpusDocInstance:
    id : str
    text : str
    title : str

@dataclass
class GPLNFCorpusQrelInstance:
    qid : str
    did : str
    score : int

@dataclass
class GPLNFCorpusHnegInstance:
    qid : str
    did : str

@dataclass
class GPLNFCorpusTripleInstance:
    qid : str
    pos : str
    neg : str
    score : float

class GPLNFCorpusDataLoader(GPLDataLoader):
    def __init__(self, *args, **kwargs):
        super().__init__('gpl/nfcorpus', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> GPLNFCorpusQueryInstance:
        return GPLNFCorpusQueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> GPLNFCorpusDocInstance:
        return GPLNFCorpusDocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> GPLNFCorpusQrelInstance:
        return GPLNFCorpusQrelInstance(**kwargs)

    def make_hneg_instance(self, **kwargs) -> GPLNFCorpusHnegInstance:
        return GPLNFCorpusHnegInstance(**kwargs)

    def make_triple_instance(self, **kwargs) -> GPLNFCorpusTripleInstance:
        return GPLNFCorpusTripleInstance(**kwargs)

    def __str__(self) -> str:
        return 'GPLNFCorpusDataLoader()'

    def __repr__(self) -> str:
        return 'GPLNFCorpusDataLoader()'
