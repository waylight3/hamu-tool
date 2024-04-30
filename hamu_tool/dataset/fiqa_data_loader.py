from .data_loader_base import DataLoaderQDRBase
from dataclasses import dataclass
from typing import Iterator

@dataclass
class FiQAQueryInstance:
    id : str
    text : str

@dataclass
class FiQADocInstance:
    id : str
    text : str

@dataclass
class FiQAQrelInstance:
    qid : str
    did : str
    score : int

class FiQADataLoader(DataLoaderQDRBase):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/fiqa', *args, **kwargs)

    def get_query(self, qid : str | int) -> FiQAQueryInstance:
        query = self.reader_query[qid]
        instance = FiQAQueryInstance(id=query['id'], text=query['text'])
        return instance

    def get_queries(self) -> Iterator[FiQAQueryInstance]:
        for query in self.reader_query:
            instance = FiQAQueryInstance(id=query['id'], text=query['text'])
            yield instance

    def get_doc(self, did : str | int) -> FiQADocInstance:
        doc = self.reader_doc[did]
        instance = FiQADocInstance(id=doc['id'], text=doc['text'])
        return instance

    def get_docs(self) -> Iterator[FiQADocInstance]:
        for doc in self.reader_doc:
            instance = FiQADocInstance(id=doc['id'], text=doc['text'])
            yield instance

    def get_qrel(self, mode : str, qid : str) -> list[FiQAQrelInstance]:
        if qid not in self.qrel[mode]:
            raise KeyError(f'Qrel for query [{qid}] not found')
        instances = []
        for did, score in self.qrel[mode][qid]:
            instances.append(FiQAQrelInstance(qid=qid, did=did, score=score))
        return instances

    def get_qrels(self, mode : str) -> Iterator[FiQAQrelInstance]:
        for qid, did, score in self.qrel_list[mode]:
            instance = FiQAQrelInstance(qid=qid, did=did, score=score)
            yield instance

    def __str__(self) -> str:
        return 'FiQADataLoader()'

    def __repr__(self) -> str:
        return 'FiQADataLoader()'
