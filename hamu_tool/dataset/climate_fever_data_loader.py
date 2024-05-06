from .data_loader_base import DataLoaderQDRBase
from dataclasses import dataclass
from typing import Iterator

@dataclass
class ClimateFEVERQueryInstance:
    id : str
    text : str

@dataclass
class ClimateFEVERDocInstance:
    id : str
    text : str
    title : str

@dataclass
class ClimateFEVERQrelInstance:
    qid : str
    did : str
    score : int

class ClimateFEVERDataLoader(DataLoaderQDRBase):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/climate-fever', *args, **kwargs)

    def get_query(self, qid : str | int, mode : str = None) -> ClimateFEVERQueryInstance:
        if isinstance(qid, int):
            qid = self.get_qid(qid, mode)
        query = self.reader_query[qid]
        instance = ClimateFEVERQueryInstance(id=query['id'], text=query['text'])
        return instance

    def get_queries(self, mode : str = None) -> Iterator[ClimateFEVERQueryInstance]:
        if not mode:
            for query in self.reader_query:
                instance = ClimateFEVERQueryInstance(id=query['id'], text=query['text'])
                yield instance
        else:
            for qid in self.qid_list[mode]:
                query = self.reader_query[qid]
                instance = ClimateFEVERQueryInstance(id=query['id'], text=query['text'])
                yield instance

    def get_doc(self, did : str | int, mode : str = None) -> ClimateFEVERDocInstance:
        if isinstance(did, int):
            did = self.get_did(did, mode)
        doc = self.reader_doc[did]
        instance = ClimateFEVERDocInstance(id=doc['id'], text=doc['text'], title=doc['title'])
        return instance

    def get_docs(self, mode : str = None) -> Iterator[ClimateFEVERDocInstance]:
        if not mode:
            for doc in self.reader_doc:
                instance = ClimateFEVERDocInstance(id=doc['id'], text=doc['text'], title=doc['title'])
                yield instance
        else:
            for did in self.did_list[mode]:
                doc = self.reader_doc[did]
                instance = ClimateFEVERDocInstance(id=doc['id'], text=doc['text'], title=doc['title'])
                yield instance

    def get_qrel(self, mode : str, qid : str) -> list[ClimateFEVERQrelInstance]:
        if qid not in self.qrel[mode]:
            raise KeyError(f'Qrel for query [{qid}] not found')
        instances = []
        for did, score in self.qrel[mode][qid]:
            instances.append(ClimateFEVERQrelInstance(qid=qid, did=did, score=score))
        return instances

    def get_qrels(self, mode : str) -> Iterator[ClimateFEVERQrelInstance]:
        for qid, did, score in self.qrel_list[mode]:
            instance = ClimateFEVERQrelInstance(qid=qid, did=did, score=score)
            yield instance

    def get_drel(self, mode : str, did : str) -> list[ClimateFEVERQrelInstance]:
        if did not in self.drel[mode]:
            raise KeyError(f'Drel for document [{did}] not found')
        instances = []
        for qid, score in self.drel[mode][did]:
            instances.append(ClimateFEVERQrelInstance(qid=qid, did=did, score=score))
        return instances

    def get_drels(self, mode : str) -> Iterator[ClimateFEVERQrelInstance]:
        return self.get_qrels(mode)

    def __str__(self) -> str:
        return 'ClimateFEVERDataLoader()'

    def __repr__(self) -> str:
        return 'ClimateFEVERDataLoader()'
