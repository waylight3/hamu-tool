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

    def get_query(self, qid : str | int) -> ClimateFEVERQueryInstance:
        query = self.reader_query[qid]
        instance = ClimateFEVERQueryInstance(id=query['id'], text=query['text'])
        return instance

    def get_queries(self) -> Iterator[ClimateFEVERQueryInstance]:
        for query in self.reader_query:
            instance = ClimateFEVERQueryInstance(id=query['id'], text=query['text'])
            yield instance

    def get_doc(self, did : str | int) -> ClimateFEVERDocInstance:
        doc = self.reader_doc[did]
        instance = ClimateFEVERDocInstance(id=doc['id'], text=doc['text'], title=doc['title'])
        return instance

    def get_docs(self) -> Iterator[ClimateFEVERDocInstance]:
        for doc in self.reader_doc:
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

    def __str__(self) -> str:
        return 'ClimateFEVERDataLoader()'

    def __repr__(self) -> str:
        return 'ClimateFEVERDataLoader()'
