from .data_loader_base import DataLoaderQDRBase
from dataclasses import dataclass
from typing import Iterator

@dataclass
class SciDocsQueryInstance:
    id : str
    text : str
    authors : list[str]
    year : int
    cited_by : list[str]
    references : list[str]

@dataclass
class SciDocsDocInstance:
    id : str
    text : str
    title : str
    authors : list[str]
    year : int
    cited_by : list[str]
    references : list[str]

@dataclass
class SciDocsQrelInstance:
    qid : str
    did : str
    score : int

class SciDocsDataLoader(DataLoaderQDRBase):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/scidocs', *args, **kwargs)

    def get_query(self, qid : str | int, mode : str = None) -> SciDocsQueryInstance:
        if isinstance(qid, int):
            qid = self.get_qid(qid, mode)
        query = self.reader_query[qid]
        instance = SciDocsQueryInstance(id=query['id'], text=query['text'], authors=query['authors'], year=query['year'], cited_by=query['cited_by'], references=query['references'])
        return instance

    def get_queries(self, mode : str = None) -> Iterator[SciDocsQueryInstance]:
        if not mode:
            for query in self.reader_query:
                instance = SciDocsQueryInstance(id=query['id'], text=query['text'], authors=query['authors'], year=query['year'], cited_by=query['cited_by'], references=query['references'])
                yield instance
        else:
            for qid in self.qid_list[mode]:
                query = self.reader_query[qid]
                instance = SciDocsQueryInstance(id=query['id'], text=query['text'], authors=query['authors'], year=query['year'], cited_by=query['cited_by'], references=query['references'])
                yield instance

    def get_doc(self, did : str | int, mode : str = None) -> SciDocsDocInstance:
        if isinstance(did, int):
            did = self.get_did(did, mode)
        doc = self.reader_doc[did]
        instance = SciDocsDocInstance(id=doc['id'], text=doc['text'], title=doc['title'], authors=doc['authors'], year=doc['year'], cited_by=doc['cited_by'], references=doc['references'])
        return instance

    def get_docs(self, mode : str = None) -> Iterator[SciDocsDocInstance]:
        if not mode:
            for doc in self.reader_doc:
                instance = SciDocsDocInstance(id=doc['id'], text=doc['text'], title=doc['title'], authors=doc['authors'], year=doc['year'], cited_by=doc['cited_by'], references=doc['references'])
                yield instance
        else:
            for did in self.did_list[mode]:
                doc = self.reader_doc[did]
                instance = SciDocsDocInstance(id=doc['id'], text=doc['text'], title=doc['title'], authors=doc['authors'], year=doc['year'], cited_by=doc['cited_by'], references=doc['references'])
                yield instance

    def get_qrel(self, mode : str, qid : str) -> list[SciDocsQrelInstance]:
        if qid not in self.qrel[mode]:
            raise KeyError(f'Qrel for query [{qid}] not found')
        instances = []
        for did, score in self.qrel[mode][qid]:
            instances.append(SciDocsQrelInstance(qid=qid, did=did, score=score))
        return instances

    def get_qrels(self, mode : str) -> Iterator[SciDocsQrelInstance]:
        for qid, did, score in self.qrel_list[mode]:
            instance = SciDocsQrelInstance(qid=qid, did=did, score=score)
            yield instance

    def get_drel(self, mode : str, did : str) -> list[SciDocsQrelInstance]:
        if did not in self.drel[mode]:
            raise KeyError(f'Drel for document [{did}] not found')
        instances = []
        for qid, score in self.drel[mode][did]:
            instances.append(SciDocsQrelInstance(qid=qid, did=did, score=score))
        return instances

    def get_drels(self, mode : str) -> Iterator[SciDocsQrelInstance]:
        return self.get_qrels(mode)

    def __str__(self) -> str:
        return 'SciDocsDataLoader()'

    def __repr__(self) -> str:
        return 'SciDocsDataLoader()'
