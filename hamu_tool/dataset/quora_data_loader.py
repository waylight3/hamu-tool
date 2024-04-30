from .data_loader_base import DataLoaderQDRBase
from dataclasses import dataclass
from typing import Iterator

@dataclass
class QuoraQueryInstance:
    id : str
    text : str

@dataclass
class QuoraDocInstance:
    id : str
    text : str

@dataclass
class QuoraQrelInstance:
    qid : str
    did : str
    score : int

class QuoraDataLoader(DataLoaderQDRBase):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/quora', *args, **kwargs)

    def get_query(self, qid : str | int) -> QuoraQueryInstance:
        query = self.reader_query[qid]
        instance = QuoraQueryInstance(id=query['id'], text=query['text'])
        return instance

    def get_queries(self) -> Iterator[QuoraQueryInstance]:
        for query in self.reader_query:
            instance = QuoraQueryInstance(id=query['id'], text=query['text'])
            yield instance

    def get_doc(self, did : str | int) -> QuoraDocInstance:
        doc = self.reader_doc[did]
        instance = QuoraDocInstance(id=doc['id'], text=doc['text'])
        return instance

    def get_docs(self) -> Iterator[QuoraDocInstance]:
        for doc in self.reader_doc:
            instance = QuoraDocInstance(id=doc['id'], text=doc['text'])
            yield instance

    def get_qrel(self, qid : str, mode : str) -> list[QuoraQrelInstance]:
        if qid not in self.qrel[mode]:
            raise KeyError(f'Qrel for query [{qid}] not found')
        instances = []
        for did, score in self.qrel[mode][qid]:
            instances.append(QuoraQrelInstance(qid=qid, did=did, score=score))
        return instances

    def get_qrels(self, mode : str) -> Iterator[QuoraQrelInstance]:
        for qid, did, score in self.qrel_list[mode]:
            instance = QuoraQrelInstance(qid=qid, did=did, score=score)
            yield instance

    def __str__(self) -> str:
        return 'QuoraDataLoader()'

    def __repr__(self) -> str:
        return 'QuoraDataLoader()'
