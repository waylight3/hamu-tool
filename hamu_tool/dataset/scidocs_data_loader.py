from .data_loader_base import DataLoaderQDRBase
from dataclasses import dataclass
from typing import Iterator

@dataclass
class SciDocsQueryInstance:
    id : str
    text : str
    year : int
    authors : list[str]
    cited_by : list[str]
    references : list[str]

@dataclass
class SciDocsDocInstance:
    id : str
    text : str
    title : str
    year : int
    authors : list[str]
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

    def get_query(self, qid : str | int) -> SciDocsQueryInstance:
        query = self.reader_query[qid]
        instance = SciDocsQueryInstance(id=query['id'], text=query['text'], year=query['year'], authors=query['authors'], cited_by=query['cited_by'], references=query['references'])
        return instance

    def get_queries(self) -> Iterator[SciDocsQueryInstance]:
        for query in self.reader_query:
            instance = SciDocsQueryInstance(id=query['id'], text=query['text'], year=query['year'], authors=query['authors'], cited_by=query['cited_by'], references=query['references'])
            yield instance

    def get_doc(self, did : str | int) -> SciDocsDocInstance:
        doc = self.reader_doc[did]
        instance = SciDocsDocInstance(id=doc['id'], text=doc['text'], title=doc['title'], year=doc['year'], authors=doc['authors'], cited_by=doc['cited_by'], references=doc['references'])
        return instance

    def get_docs(self) -> Iterator[SciDocsDocInstance]:
        for doc in self.reader_doc:
            instance = SciDocsDocInstance(id=doc['id'], text=doc['text'], title=doc['title'], year=doc['year'], authors=doc['authors'], cited_by=doc['cited_by'], references=doc['references'])
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

    def __str__(self) -> str:
        return 'SciDocsDataLoader()'

    def __repr__(self) -> str:
        return 'SciDocsDataLoader()'
