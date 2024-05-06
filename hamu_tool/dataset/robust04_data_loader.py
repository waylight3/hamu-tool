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

    def get_query(self, qid : str | int, mode : str = None) -> Robust04QueryInstance:
        if isinstance(qid, int):
            qid = self.get_qid(qid, mode)
        query = self.reader_query[qid]
        instance = Robust04QueryInstance(id=query['id'], text=query['text'])
        return instance

    def get_queries(self, mode : str = None) -> Iterator[Robust04QueryInstance]:
        if not mode:
            for query in self.reader_query:
                instance = Robust04QueryInstance(id=query['id'], text=query['text'])
                yield instance
        else:
            for qid in self.qid_list[mode]:
                query = self.reader_query[qid]
                instance = Robust04QueryInstance(id=query['id'], text=query['text'])
                yield instance

    def get_doc(self, did : str | int, mode : str = None) -> Robust04DocInstance:
        if isinstance(did, int):
            did = self.get_did(did, mode)
        doc = self.reader_doc[did]
        instance = Robust04DocInstance(id=doc['id'], text=doc['text'])
        return instance

    def get_docs(self, mode : str = None) -> Iterator[Robust04DocInstance]:
        if not mode:
            for doc in self.reader_doc:
                instance = Robust04DocInstance(id=doc['id'], text=doc['text'])
                yield instance
        else:
            for did in self.did_list[mode]:
                doc = self.reader_doc[did]
                instance = Robust04DocInstance(id=doc['id'], text=doc['text'])
                yield instance

    def get_qrel(self, mode : str, qid : str) -> list[Robust04QrelInstance]:
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

    def get_drel(self, mode : str, did : str) -> list[Robust04QrelInstance]:
        if did not in self.drel[mode]:
            raise KeyError(f'Drel for document [{did}] not found')
        instances = []
        for qid, score in self.drel[mode][did]:
            instances.append(Robust04QrelInstance(qid=qid, did=did, score=score))
        return instances

    def get_drels(self, mode : str) -> Iterator[Robust04QrelInstance]:
        return self.get_qrels(mode)

    def __str__(self) -> str:
        return 'Robust04DataLoader()'

    def __repr__(self) -> str:
        return 'Robust04DataLoader()'
