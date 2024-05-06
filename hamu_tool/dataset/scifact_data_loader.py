from .data_loader_base import DataLoaderQDRBase
from dataclasses import dataclass
from typing import Iterator

@dataclass
class SciFactQueryInstance:
    id : str
    text : str

@dataclass
class SciFactDocInstance:
    id : str
    text : str
    title : str

@dataclass
class SciFactQrelInstance:
    qid : str
    did : str
    score : int

class SciFactDataLoader(DataLoaderQDRBase):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/scifact', *args, **kwargs)

    def get_query(self, qid : str | int, mode : str = None) -> SciFactQueryInstance:
        if isinstance(qid, int):
            qid = self.get_qid(qid, mode)
        query = self.reader_query[qid]
        instance = SciFactQueryInstance(id=query['id'], text=query['text'])
        return instance

    def get_queries(self, mode : str = None) -> Iterator[SciFactQueryInstance]:
        if not mode:
            for query in self.reader_query:
                instance = SciFactQueryInstance(id=query['id'], text=query['text'])
                yield instance
        else:
            for qid in self.qid_list[mode]:
                query = self.reader_query[qid]
                instance = SciFactQueryInstance(id=query['id'], text=query['text'])
                yield instance

    def get_doc(self, did : str | int, mode : str = None) -> SciFactDocInstance:
        if isinstance(did, int):
            did = self.get_did(did, mode)
        doc = self.reader_doc[did]
        instance = SciFactDocInstance(id=doc['id'], text=doc['text'], title=doc['title'])
        return instance

    def get_docs(self, mode : str = None) -> Iterator[SciFactDocInstance]:
        if not mode:
            for doc in self.reader_doc:
                instance = SciFactDocInstance(id=doc['id'], text=doc['text'], title=doc['title'])
                yield instance
        else:
            for did in self.did_list[mode]:
                doc = self.reader_doc[did]
                instance = SciFactDocInstance(id=doc['id'], text=doc['text'], title=doc['title'])
                yield instance

    def get_qrel(self, mode : str, qid : str) -> list[SciFactQrelInstance]:
        if qid not in self.qrel[mode]:
            raise KeyError(f'Qrel for query [{qid}] not found')
        instances = []
        for did, score in self.qrel[mode][qid]:
            instances.append(SciFactQrelInstance(qid=qid, did=did, score=score))
        return instances

    def get_qrels(self, mode : str) -> Iterator[SciFactQrelInstance]:
        for qid, did, score in self.qrel_list[mode]:
            instance = SciFactQrelInstance(qid=qid, did=did, score=score)
            yield instance

    def get_drel(self, mode : str, did : str) -> list[SciFactQrelInstance]:
        if did not in self.drel[mode]:
            raise KeyError(f'Drel for document [{did}] not found')
        instances = []
        for qid, score in self.drel[mode][did]:
            instances.append(SciFactQrelInstance(qid=qid, did=did, score=score))
        return instances

    def get_drels(self, mode : str) -> Iterator[SciFactQrelInstance]:
        return self.get_qrels(mode)

    def __str__(self) -> str:
        return 'SciFactDataLoader()'

    def __repr__(self) -> str:
        return 'SciFactDataLoader()'
