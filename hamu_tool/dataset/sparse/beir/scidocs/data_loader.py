from ..data_loader import BEIRDataLoader
from dataclasses import dataclass

@dataclass
class BEIRSciDocsQueryInstance:
    id : str
    text : str
    authors : list[str]
    year : int
    cited_by : list[str]
    references : list[str]

@dataclass
class BEIRSciDocsDocInstance:
    id : str
    text : str
    title : str
    authors : list[str]
    year : int
    cited_by : list[str]
    references : list[str]

@dataclass
class BEIRSciDocsQrelInstance:
    qid : str
    did : str
    score : int

class BEIRSciDocsDataLoader(BEIRDataLoader):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/scidocs', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> BEIRSciDocsQueryInstance:
        return BEIRSciDocsQueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> BEIRSciDocsDocInstance:
        return BEIRSciDocsDocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> BEIRSciDocsQrelInstance:
        return BEIRSciDocsQrelInstance(**kwargs)

    def __str__(self) -> str:
        return 'BEIRSciDocsDataLoader()'

    def __repr__(self) -> str:
        return 'BEIRSciDocsDataLoader()'
