from .data_loader_base import DataLoaderQDRBase
from dataclasses import dataclass
from typing import Iterator

@dataclass
class FEVERQueryInstance:
    id : str
    text : str

@dataclass
class FEVERDocInstance:
    id : str
    text : str
    title : str

@dataclass
class FEVERQrelInstance:
    qid : str
    did : str
    score : int

class FEVERDataLoader(DataLoaderQDRBase):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/fever', *args, **kwargs)

    def get_query(self, qid : str | int) -> FEVERQueryInstance:
        query = self.reader_query[qid]
        instance = FEVERQueryInstance(id=query['id'], text=query['text'])
        return instance

    def get_queries(self) -> Iterator[FEVERQueryInstance]:
        for query in self.reader_query:
            instance = FEVERQueryInstance(id=query['id'], text=query['text'])
            yield instance

    def get_doc(self, did : str | int) -> FEVERDocInstance:
        doc = self.reader_doc[did]
        instance = FEVERDocInstance(id=doc['id'], text=doc['text'], title=doc['title'])
        return instance

    def get_docs(self) -> Iterator[FEVERDocInstance]:
        for doc in self.reader_doc:
            instance = FEVERDocInstance(id=doc['id'], text=doc['text'], title=doc['title'])
            yield instance

    def get_qrel(self, qid : str, mode : str) -> list[FEVERQrelInstance]:
        if qid not in self.qrel[mode]:
            raise KeyError(f'Qrel for query [{qid}] not found')
        instances = []
        for did, score in self.qrel[mode][qid]:
            instances.append(FEVERQrelInstance(qid=qid, did=did, score=score))
        return instances

    def get_qrels(self, mode : str) -> Iterator[FEVERQrelInstance]:
        for qid, did, score in self.qrel_list[mode]:
            instance = FEVERQrelInstance(qid=qid, did=did, score=score)
            yield instance

    def __str__(self) -> str:
        return 'FEVERDataLoader()'

    def __repr__(self) -> str:
        return 'FEVERDataLoader()'
