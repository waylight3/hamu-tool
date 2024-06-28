from ..data_loader import BEIRDataLoader
from dataclasses import dataclass

@dataclass
class BEIRNFCorpusQueryInstance:
    id : str
    text : str
    url : str

@dataclass
class BEIRNFCorpusDocInstance:
    id : str
    text : str
    title : str
    url : str

@dataclass
class BEIRNFCorpusQrelInstance:
    qid : str
    did : str
    score : int

class BEIRNFCorpusDataLoader(BEIRDataLoader):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/nfcorpus', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> BEIRNFCorpusQueryInstance:
        return BEIRNFCorpusQueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> BEIRNFCorpusDocInstance:
        return BEIRNFCorpusDocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> BEIRNFCorpusQrelInstance:
        return BEIRNFCorpusQrelInstance(**kwargs)

    def __str__(self) -> str:
        return 'BEIRNFCorpusDataLoader()'

    def __repr__(self) -> str:
        return 'BEIRNFCorpusDataLoader()'
