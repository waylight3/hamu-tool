from .data_loader_base import DataLoaderQDRBase
from dataclasses import dataclass
from typing import Iterator

@dataclass
class HotpotQAQueryInstance:
    id : str
    text : str

@dataclass
class HotpotQADocInstance:
    id : str
    text : str
    title : str
    url : str

@dataclass
class HotpotQAQrelInstance:
    qid : str
    did : str
    score : int

class HotpotQADataLoader(DataLoaderQDRBase):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/hotpotqa', *args, **kwargs)

    def make_query_instance(self, **kwargs) -> HotpotQAQueryInstance:
        return HotpotQAQueryInstance(**kwargs)

    def make_doc_instance(self, **kwargs) -> HotpotQADocInstance:
        return HotpotQADocInstance(**kwargs)

    def make_qrel_instance(self, **kwargs) -> HotpotQAQrelInstance:
        return HotpotQAQrelInstance(**kwargs)

    def __str__(self) -> str:
        return 'HotpotQADataLoader()'

    def __repr__(self) -> str:
        return 'HotpotQADataLoader()'
