from .data_loader_base import DataLoaderQDRBase
from dataclasses import dataclass
from typing import Iterator

@dataclass
class DBPediaQueryInstance:
    id : str
    text : str

@dataclass
class DBPediaDocInstance:
    id : str
    text : str
    title : str
    url : str

@dataclass
class DBPediaQrelInstance:
    qid : str
    did : str
    score : int

class DBPediaDataLoader(DataLoaderQDRBase):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/dbpedia', *args, **kwargs)

    def get_query(self, qid : str | int, mode : str = None) -> DBPediaQueryInstance:
        if isinstance(qid, int):
            qid = self.get_qid(qid, mode)
        query = self.reader_query[qid]
        instance = DBPediaQueryInstance(id=query['id'], text=query['text'])
        return instance

    def get_queries(self, mode : str = None) -> Iterator[DBPediaQueryInstance]:
        if not mode:
            for query in self.reader_query:
                instance = DBPediaQueryInstance(id=query['id'], text=query['text'])
                yield instance
        else:
            for qid in self.qid_list[mode]:
                query = self.reader_query[qid]
                instance = DBPediaQueryInstance(id=query['id'], text=query['text'])
                yield instance

    def get_doc(self, did : str | int, mode : str = None) -> DBPediaDocInstance:
        if isinstance(did, int):
            did = self.get_did(did, mode)
        doc = self.reader_doc[did]
        instance = DBPediaDocInstance(id=doc['id'], text=doc['text'], title=doc['title'], url=doc['url'])
        return instance

    def get_docs(self, mode : str = None) -> Iterator[DBPediaDocInstance]:
        if not mode:
            for doc in self.reader_doc:
                instance = DBPediaDocInstance(id=doc['id'], text=doc['text'], title=doc['title'], url=doc['url'])
                yield instance
        else:
            for did in self.did_list[mode]:
                doc = self.reader_doc[did]
                instance = DBPediaDocInstance(id=doc['id'], text=doc['text'], title=doc['title'], url=doc['url'])
                yield instance

    def get_qrel(self, mode : str, qid : str) -> list[DBPediaQrelInstance]:
        if qid not in self.qrel[mode]:
            raise KeyError(f'Qrel for query [{qid}] not found')
        instances = []
        for did, score in self.qrel[mode][qid]:
            instances.append(DBPediaQrelInstance(qid=qid, did=did, score=score))
        return instances

    def get_qrels(self, mode : str) -> Iterator[DBPediaQrelInstance]:
        for qid, did, score in self.qrel_list[mode]:
            instance = DBPediaQrelInstance(qid=qid, did=did, score=score)
            yield instance

    def get_drel(self, mode : str, did : str) -> list[DBPediaQrelInstance]:
        if did not in self.drel[mode]:
            raise KeyError(f'Drel for document [{did}] not found')
        instances = []
        for qid, score in self.drel[mode][did]:
            instances.append(DBPediaQrelInstance(qid=qid, did=did, score=score))
        return instances

    def get_drels(self, mode : str) -> Iterator[DBPediaQrelInstance]:
        return self.get_qrels(mode)

    def __str__(self) -> str:
        return 'DBPediaDataLoader()'

    def __repr__(self) -> str:
        return 'DBPediaDataLoader()'
