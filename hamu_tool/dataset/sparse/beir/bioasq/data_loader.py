from ..data_loader import BEIRDataLoader
from dataclasses import dataclass

@dataclass
class BEIRBioASQQueryInstance:
    id : str
    text : str

@dataclass
class BEIRBioASQDocInstance:
    id : str
    text : str
    title : str
    journal : str
    year : int
    pmid : str
    mesh_major : list[str]

@dataclass
class BEIRBioASQQrelInstance:
    qid : str
    did : str
    score : int

class BEIRBioASQDataLoader(BEIRDataLoader):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/bioasq', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> BEIRBioASQQueryInstance:
        return BEIRBioASQQueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> BEIRBioASQDocInstance:
        return BEIRBioASQDocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> BEIRBioASQQrelInstance:
        return BEIRBioASQQrelInstance(**kwargs)

    def __str__(self) -> str:
        return 'BEIRBioASQDataLoader()'

    def __repr__(self) -> str:
        return 'BEIRBioASQDataLoader()'
