from .data_loader_base import DataLoaderQDRBase
from dataclasses import dataclass
from typing import Iterator

@dataclass
class Touchev2QueryInstance:
    id : str
    text : str
    description : str
    narrative : str

@dataclass
class Touchev2DocInstance:
    id : str
    text : str
    title : str
    stance : str
    url : str

@dataclass
class Touchev2QrelInstance:
    qid : str
    did : str
    score : int

class Touchev2DataLoader(DataLoaderQDRBase):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/touche-v2', *args, **kwargs)

    def get_query(self, qid : str | int) -> Touchev2QueryInstance:
        query = self.reader_query[qid]
        instance = Touchev2QueryInstance(id=query['id'], text=query['text'], description=query['description'], narrative=query['narrative'])
        return instance

    def get_queries(self) -> Iterator[Touchev2QueryInstance]:
        for query in self.reader_query:
            instance = Touchev2QueryInstance(id=query['id'], text=query['text'], description=query['description'], narrative=query['narrative'])
            yield instance

    def get_doc(self, did : str | int) -> Touchev2DocInstance:
        doc = self.reader_doc[did]
        instance = Touchev2DocInstance(id=doc['id'], text=doc['text'], title=doc['title'], stance=doc['stance'], url=doc['url'])
        return instance

    def get_docs(self) -> Iterator[Touchev2DocInstance]:
        for doc in self.reader_doc:
            instance = Touchev2DocInstance(id=doc['id'], text=doc['text'], title=doc['title'], stance=doc['stance'], url=doc['url'])
            yield instance

    def get_qrel(self, qid : str, mode : str) -> list[Touchev2QrelInstance]:
        if qid not in self.qrel[mode]:
            raise KeyError(f'Qrel for query [{qid}] not found')
        instances = []
        for did, score in self.qrel[mode][qid]:
            instances.append(Touchev2QrelInstance(qid=qid, did=did, score=score))
        return instances

    def get_qrels(self, mode : str) -> Iterator[Touchev2QrelInstance]:
        for qid, did, score in self.qrel_list[mode]:
            instance = Touchev2QrelInstance(qid=qid, did=did, score=score)
            yield instance

    def __str__(self) -> str:
        return 'Touchev2DataLoader()'

    def __repr__(self) -> str:
        return 'Touchev2DataLoader()'
