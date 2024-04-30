from .data_loader_base import DataLoaderQDRBase
from dataclasses import dataclass
from typing import Iterator

@dataclass
class Robust04QueryInstance:
    id : str
    text : str

@dataclass
class Robust04DocInstance:
    id : str
    text : str

@dataclass
class Robust04QrelInstance:
    qid : str
    did : str
    score : int

class Robust04DataLoader(DataLoaderQDRBase):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/robust04', *args, **kwargs)

    def get_query(self, qid : str | int) -> Robust04QueryInstance:
        query = self.reader_query[qid]
        instance = Robust04QueryInstance(id=query['id'], text=query['text'])
        return instance

    def get_queries(self) -> Iterator[Robust04QueryInstance]:
        for query in self.reader_query:
            instance = Robust04QueryInstance(id=query['id'], text=query['text'])
            yield instance

    def get_doc(self, did : str | int) -> Robust04DocInstance:
        doc = self.reader_doc[did]
        instance = Robust04DocInstance(id=doc['id'], text=doc['text'])
        return instance

    def get_docs(self) -> Iterator[Robust04DocInstance]:
        for doc in self.reader_doc:
            instance = Robust04DocInstance(id=doc['id'], text=doc['text'])
            yield instance

    def get_qrel(self, qid : str, mode : str) -> list[Robust04QrelInstance]:
        if qid not in self.qrel[mode]:
            raise KeyError(f'Qrel for query [{qid}] not found')
        instances = []
        for did, score in self.qrel[mode][qid]:
            instances.append(Robust04QrelInstance(qid=qid, did=did, score=score))
        return instances

    def get_qrels(self, mode : str) -> Iterator[Robust04QrelInstance]:
        for qid, did, score in self.qrel_list[mode]:
            instance = Robust04QrelInstance(qid=qid, did=did, score=score)
            yield instance

    def __str__(self) -> str:
        return 'Robust04DataLoader()'

    def __repr__(self) -> str:
        return 'Robust04DataLoader()'
