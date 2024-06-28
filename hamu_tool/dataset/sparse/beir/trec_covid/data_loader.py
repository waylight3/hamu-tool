from ..data_loader import BEIRDataLoader
from dataclasses import dataclass

@dataclass
class BEIRTrecCovidQueryInstance:
    id : str
    text : str
    narrative : str

@dataclass
class BEIRTrecCovidDocInstance:
    id : str
    text : str
    title : str
    url : str
    pubmed_id : str

@dataclass
class BEIRTrecCovidQrelInstance:
    qid : str
    did : str
    score : int

class BEIRTrecCovidDataLoader(BEIRDataLoader):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/trec-covid', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> BEIRTrecCovidQueryInstance:
        return BEIRTrecCovidQueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> BEIRTrecCovidDocInstance:
        return BEIRTrecCovidDocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> BEIRTrecCovidQrelInstance:
        return BEIRTrecCovidQrelInstance(**kwargs)

    def __str__(self) -> str:
        return 'BEIRTrecCovidDataLoader()'

    def __repr__(self) -> str:
        return 'BEIRTrecCovidDataLoader()'
