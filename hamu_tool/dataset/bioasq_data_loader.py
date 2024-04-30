from .data_loader_base import DataLoaderQDRBase
from dataclasses import dataclass
from typing import Iterator

@dataclass
class BioASQQueryInstance:
    id : str
    text : str

@dataclass
class BioASQDocInstance:
    id : str
    text : str
    title : str
    journal : str
    year : int
    pmid : str
    mesh_major : list[str]

@dataclass
class BioASQQrelInstance:
    qid : str
    did : str
    score : int

class BioASQDataLoader(DataLoaderQDRBase):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/bioasq', *args, **kwargs)

    def get_query(self, qid : str | int) -> BioASQQueryInstance:
        query = self.reader_query[qid]
        instance = BioASQQueryInstance(id=query['id'], text=query['text'])
        return instance

    def get_queries(self) -> Iterator[BioASQQueryInstance]:
        for query in self.reader_query:
            instance = BioASQQueryInstance(id=query['id'], text=query['text'])
            yield instance

    def get_doc(self, did : str | int) -> BioASQDocInstance:
        doc = self.reader_doc[did]
        instance = BioASQDocInstance(id=doc['id'], text=doc['text'], title=doc['title'], journal=doc['journal'], year=doc['year'], pmid=doc['pmid'], mesh_major=doc['mesh_major'])
        return instance

    def get_docs(self) -> Iterator[BioASQDocInstance]:
        for doc in self.reader_doc:
            instance = BioASQDocInstance(id=doc['id'], text=doc['text'], title=doc['title'], journal=doc['journal'], year=doc['year'], pmid=doc['pmid'], mesh_major=doc['mesh_major'])
            yield instance

    def get_qrel(self, qid : str, mode : str) -> list[BioASQQrelInstance]:
        if qid not in self.qrel[mode]:
            raise KeyError(f'Qrel for query [{qid}] not found')
        instances = []
        for did, score in self.qrel[mode][qid]:
            instances.append(BioASQQrelInstance(qid=qid, did=did, score=score))
        return instances

    def get_qrels(self, mode : str) -> Iterator[BioASQQrelInstance]:
        for qid, did, score in self.qrel_list[mode]:
            instance = BioASQQrelInstance(qid=qid, did=did, score=score)
            yield instance

    def __str__(self) -> str:
        return 'BioASQDataLoader()'

    def __repr__(self) -> str:
        return 'BioASQDataLoader()'
