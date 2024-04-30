from .data_loader_base import DataLoaderQDRBase
from dataclasses import dataclass
from typing import Iterator

@dataclass
class NQQueryInstance:
    id : str
    text : str

@dataclass
class NQDocInstance:
    id : str
    text : str
    title : str

@dataclass
class NQQrelInstance:
    qid : str
    did : str
    score : int

class NQDataLoader(DataLoaderQDRBase):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/nq', *args, **kwargs)

    def get_query(self, qid : str | int) -> NQQueryInstance:
        query = self.reader_query[qid]
        instance = NQQueryInstance(id=query['id'], text=query['text'])
        return instance

    def get_queries(self) -> Iterator[NQQueryInstance]:
        for query in self.reader_query:
            instance = NQQueryInstance(id=query['id'], text=query['text'])
            yield instance

    def get_doc(self, did : str | int) -> NQDocInstance:
        doc = self.reader_doc[did]
        instance = NQDocInstance(id=doc['id'], text=doc['text'], title=doc['title'])
        return instance

    def get_docs(self) -> Iterator[NQDocInstance]:
        for doc in self.reader_doc:
            instance = NQDocInstance(id=doc['id'], text=doc['text'], title=doc['title'])
            yield instance

    def get_qrel(self, mode : str, qid : str) -> list[NQQrelInstance]:
        if qid not in self.qrel[mode]:
            raise KeyError(f'Qrel for query [{qid}] not found')
        instances = []
        for did, score in self.qrel[mode][qid]:
            instances.append(NQQrelInstance(qid=qid, did=did, score=score))
        return instances

    def get_qrels(self, mode : str) -> Iterator[NQQrelInstance]:
        for qid, did, score in self.qrel_list[mode]:
            instance = NQQrelInstance(qid=qid, did=did, score=score)
            yield instance

    def __str__(self) -> str:
        return 'NQDataLoader()'

    def __repr__(self) -> str:
        return 'NQDataLoader()'
