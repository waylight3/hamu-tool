from .data_loader_base import DataLoaderQDRBase
from dataclasses import dataclass
from typing import Iterator

@dataclass
class Signal1MQueryInstance:
    id : str
    text : str

@dataclass
class Signal1MDocInstance:
    id : str
    text : str

@dataclass
class Signal1MQrelInstance:
    qid : str
    did : str
    score : int

class Signal1MDataLoader(DataLoaderQDRBase):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/signal1m', *args, **kwargs)

    def get_query(self, qid : str | int, mode : str = None) -> Signal1MQueryInstance:
        if isinstance(qid, int):
            qid = self.get_qid(qid, mode)
        query = self.reader_query[qid]
        instance = Signal1MQueryInstance(id=query['id'], text=query['text'])
        return instance

    def get_queries(self, mode : str = None) -> Iterator[Signal1MQueryInstance]:
        if not mode:
            for query in self.reader_query:
                instance = Signal1MQueryInstance(id=query['id'], text=query['text'])
                yield instance
        else:
            for qid in self.qid_list[mode]:
                query = self.reader_query[qid]
                instance = Signal1MQueryInstance(id=query['id'], text=query['text'])
                yield instance

    def get_doc(self, did : str | int, mode : str = None) -> Signal1MDocInstance:
        if isinstance(did, int):
            did = self.get_did(did, mode)
        doc = self.reader_doc[did]
        instance = Signal1MDocInstance(id=doc['id'], text=doc['text'])
        return instance

    def get_docs(self, mode : str = None) -> Iterator[Signal1MDocInstance]:
        if not mode:
            for doc in self.reader_doc:
                instance = Signal1MDocInstance(id=doc['id'], text=doc['text'])
                yield instance
        else:
            for did in self.did_list[mode]:
                doc = self.reader_doc[did]
                instance = Signal1MDocInstance(id=doc['id'], text=doc['text'])
                yield instance

    def get_qrel(self, mode : str, qid : str) -> list[Signal1MQrelInstance]:
        if qid not in self.qrel[mode]:
            raise KeyError(f'Qrel for query [{qid}] not found')
        instances = []
        for did, score in self.qrel[mode][qid]:
            instances.append(Signal1MQrelInstance(qid=qid, did=did, score=score))
        return instances

    def get_qrels(self, mode : str) -> Iterator[Signal1MQrelInstance]:
        for qid, did, score in self.qrel_list[mode]:
            instance = Signal1MQrelInstance(qid=qid, did=did, score=score)
            yield instance

    def get_drel(self, mode : str, did : str) -> list[Signal1MQrelInstance]:
        if did not in self.drel[mode]:
            raise KeyError(f'Drel for document [{did}] not found')
        instances = []
        for qid, score in self.drel[mode][did]:
            instances.append(Signal1MQrelInstance(qid=qid, did=did, score=score))
        return instances

    def get_drels(self, mode : str) -> Iterator[Signal1MQrelInstance]:
        return self.get_qrels(mode)

    def __str__(self) -> str:
        return 'Signal1MDataLoader()'

    def __repr__(self) -> str:
        return 'Signal1MDataLoader()'
