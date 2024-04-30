from .data_loader_base import DataLoaderQDRBase
from dataclasses import dataclass
from typing import Iterator

@dataclass
class MSMARCOQueryInstance:
    id : str
    text : str

@dataclass
class MSMARCODocInstance:
    id : str
    text : str

@dataclass
class MSMARCOQrelInstance:
    qid : str
    did : str
    score : int

class MSMARCODataLoader(DataLoaderQDRBase):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/msmarco', *args, **kwargs)

    def get_query(self, qid : str | int) -> MSMARCOQueryInstance:
        query = self.reader_query[qid]
        instance = MSMARCOQueryInstance(id=query['id'], text=query['text'])
        return instance

    def get_queries(self) -> Iterator[MSMARCOQueryInstance]:
        for query in self.reader_query:
            instance = MSMARCOQueryInstance(id=query['id'], text=query['text'])
            yield instance

    def get_doc(self, did : str | int) -> MSMARCODocInstance:
        doc = self.reader_doc[did]
        instance = MSMARCODocInstance(id=doc['id'], text=doc['text'])
        return instance

    def get_docs(self) -> Iterator[MSMARCODocInstance]:
        for doc in self.reader_doc:
            instance = MSMARCODocInstance(id=doc['id'], text=doc['text'])
            yield instance

    def get_qrel(self, qid : str, mode : str) -> list[MSMARCOQrelInstance]:
        if qid not in self.qrel[mode]:
            raise KeyError(f'Qrel for query [{qid}] not found')
        instances = []
        for did, score in self.qrel[mode][qid]:
            instances.append(MSMARCOQrelInstance(qid=qid, did=did, score=score))
        return instances

    def get_qrels(self, mode : str) -> Iterator[MSMARCOQrelInstance]:
        for qid, did, score in self.qrel_list[mode]:
            instance = MSMARCOQrelInstance(qid=qid, did=did, score=score)
            yield instance

    def __str__(self) -> str:
        return 'MSMARCODataLoader()'

    def __repr__(self) -> str:
        return 'MSMARCODataLoader()'
