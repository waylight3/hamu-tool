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

    def get_query(self, qid : str | int, mode : str = None) -> Touchev2QueryInstance:
        if isinstance(qid, int):
            qid = self.get_qid(qid, mode)
        query = self.reader_query[qid]
        instance = Touchev2QueryInstance(id=query['id'], text=query['text'], description=query['description'], narrative=query['narrative'])
        return instance

    def get_queries(self, mode : str = None) -> Iterator[Touchev2QueryInstance]:
        if not mode:
            for query in self.reader_query:
                instance = Touchev2QueryInstance(id=query['id'], text=query['text'], description=query['description'], narrative=query['narrative'])
                yield instance
        else:
            for qid in self.qid_list[mode]:
                query = self.reader_query[qid]
                instance = Touchev2QueryInstance(id=query['id'], text=query['text'], description=query['description'], narrative=query['narrative'])
                yield instance

    def get_doc(self, did : str | int, mode : str = None) -> Touchev2DocInstance:
        if isinstance(did, int):
            did = self.get_did(did, mode)
        doc = self.reader_doc[did]
        instance = Touchev2DocInstance(id=doc['id'], text=doc['text'], title=doc['title'], stance=doc['stance'], url=doc['url'])
        return instance

    def get_docs(self, mode : str = None) -> Iterator[Touchev2DocInstance]:
        if not mode:
            for doc in self.reader_doc:
                instance = Touchev2DocInstance(id=doc['id'], text=doc['text'], title=doc['title'], stance=doc['stance'], url=doc['url'])
                yield instance
        else:
            for did in self.did_list[mode]:
                doc = self.reader_doc[did]
                instance = Touchev2DocInstance(id=doc['id'], text=doc['text'], title=doc['title'], stance=doc['stance'], url=doc['url'])
                yield instance

    def get_qrel(self, mode : str, qid : str) -> list[Touchev2QrelInstance]:
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

    def get_drel(self, mode : str, did : str) -> list[Touchev2QrelInstance]:
        if did not in self.drel[mode]:
            raise KeyError(f'Drel for document [{did}] not found')
        instances = []
        for qid, score in self.drel[mode][did]:
            instances.append(Touchev2QrelInstance(qid=qid, did=did, score=score))
        return instances

    def get_drels(self, mode : str) -> Iterator[Touchev2QrelInstance]:
        return self.get_qrels(mode)

    def __str__(self) -> str:
        return 'Touchev2DataLoader()'

    def __repr__(self) -> str:
        return 'Touchev2DataLoader()'
