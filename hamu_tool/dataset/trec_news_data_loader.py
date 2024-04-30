from .data_loader_base import DataLoaderQDRBase
from dataclasses import dataclass
from typing import Iterator

@dataclass
class TrecNewsQueryInstance:
    id : str
    text : str

@dataclass
class TrecNewsDocInstance:
    id : str
    text : str
    title : str
    url : str
    author : str
    type : str
    source : str
    published_date : int

@dataclass
class TrecNewsQrelInstance:
    qid : str
    did : str
    score : int

class TrecNewsDataLoader(DataLoaderQDRBase):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/trec-news', *args, **kwargs)

    def get_query(self, qid : str | int) -> TrecNewsQueryInstance:
        query = self.reader_query[qid]
        instance = TrecNewsQueryInstance(id=query['id'], text=query['text'])
        return instance

    def get_queries(self) -> Iterator[TrecNewsQueryInstance]:
        for query in self.reader_query:
            instance = TrecNewsQueryInstance(id=query['id'], text=query['text'])
            yield instance

    def get_doc(self, did : str | int) -> TrecNewsDocInstance:
        doc = self.reader_doc[did]
        instance = TrecNewsDocInstance(id=doc['id'], text=doc['text'], title=doc['title'], url=doc['url'], author=doc['author'], type=doc['type'], source=doc['source'], published_date=doc['published_date'])
        return instance

    def get_docs(self) -> Iterator[TrecNewsDocInstance]:
        for doc in self.reader_doc:
            instance = TrecNewsDocInstance(id=doc['id'], text=doc['text'], title=doc['title'], url=doc['url'], author=doc['author'], type=doc['type'], source=doc['source'], published_date=doc['published_date'])
            yield instance

    def get_qrel(self, qid : str, mode : str) -> list[TrecNewsQrelInstance]:
        if qid not in self.qrel[mode]:
            raise KeyError(f'Qrel for query [{qid}] not found')
        instances = []
        for did, score in self.qrel[mode][qid]:
            instances.append(TrecNewsQrelInstance(qid=qid, did=did, score=score))
        return instances

    def get_qrels(self, mode : str) -> Iterator[TrecNewsQrelInstance]:
        for qid, did, score in self.qrel_list[mode]:
            instance = TrecNewsQrelInstance(qid=qid, did=did, score=score)
            yield instance

    def __str__(self) -> str:
        return 'TrecNewsDataLoader()'

    def __repr__(self) -> str:
        return 'TrecNewsDataLoader()'
