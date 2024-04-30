from .data_loader_base import DataLoaderQDRBase
from dataclasses import dataclass
from typing import Iterator

@dataclass
class ToucheQueryInstance:
    id : str
    text : str
    description : str
    narrative : str

@dataclass
class ToucheDocInstance:
    id : str
    text : str
    title : str
    stance : str
    url : str

@dataclass
class ToucheQrelInstance:
    qid : str
    did : str
    score : int

class ToucheDataLoader(DataLoaderQDRBase):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/touche', *args, **kwargs)

    def get_query(self, qid : str | int) -> ToucheQueryInstance:
        query = self.reader_query[qid]
        instance = ToucheQueryInstance(id=query['id'], text=query['text'], description=query['description'], narrative=query['narrative'])
        return instance

    def get_queries(self) -> Iterator[ToucheQueryInstance]:
        for query in self.reader_query:
            instance = ToucheQueryInstance(id=query['id'], text=query['text'], description=query['description'], narrative=query['narrative'])
            yield instance

    def get_doc(self, did : str | int) -> ToucheDocInstance:
        doc = self.reader_doc[did]
        instance = ToucheDocInstance(id=doc['id'], text=doc['text'], title=doc['title'], stance=doc['stance'], url=doc['url'])
        return instance

    def get_docs(self) -> Iterator[ToucheDocInstance]:
        for doc in self.reader_doc:
            instance = ToucheDocInstance(id=doc['id'], text=doc['text'], title=doc['title'], stance=doc['stance'], url=doc['url'])
            yield instance

    def get_qrel(self, qid : str, mode : str) -> list[ToucheQrelInstance]:
        if qid not in self.qrel[mode]:
            raise KeyError(f'Qrel for query [{qid}] not found')
        instances = []
        for did, score in self.qrel[mode][qid]:
            instances.append(ToucheQrelInstance(qid=qid, did=did, score=score))
        return instances

    def get_qrels(self, mode : str) -> Iterator[ToucheQrelInstance]:
        for qid, did, score in self.qrel_list[mode]:
            instance = ToucheQrelInstance(qid=qid, did=did, score=score)
            yield instance

    def __str__(self) -> str:
        return 'ToucheDataLoader()'

    def __repr__(self) -> str:
        return 'ToucheDataLoader()'
