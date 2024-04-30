from .data_loader_base import DataLoaderQDRBase
from dataclasses import dataclass
from typing import Iterator

@dataclass
class TrecCovidQueryInstance:
    id : str
    text : str
    narrative : str

@dataclass
class TrecCovidDocInstance:
    id : str
    text : str
    title : str
    url: str
    pubmed_id : str

@dataclass
class TrecCovidQrelInstance:
    qid : str
    did : str
    score : int

class TrecCovidDataLoader(DataLoaderQDRBase):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/trec-covid', *args, **kwargs)

    def get_query(self, qid : str | int) -> TrecCovidQueryInstance:
        query = self.reader_query[qid]
        instance = TrecCovidQueryInstance(id=query['id'], text=query['text'], narrative=query['narrative'])
        return instance

    def get_queries(self) -> Iterator[TrecCovidQueryInstance]:
        for query in self.reader_query:
            instance = TrecCovidQueryInstance(id=query['id'], text=query['text'], narrative=query['narrative'])
            yield instance

    def get_doc(self, did : str | int) -> TrecCovidDocInstance:
        doc = self.reader_doc[did]
        instance = TrecCovidDocInstance(id=doc['id'], text=doc['text'], title=doc['title'], url=doc['url'], pubmed_id=doc['pubmed_id'])
        return instance

    def get_docs(self) -> Iterator[TrecCovidDocInstance]:
        for doc in self.reader_doc:
            instance = TrecCovidDocInstance(id=doc['id'], text=doc['text'], title=doc['title'], url=doc['url'], pubmed_id=doc['pubmed_id'])
            yield instance

    def get_qrel(self, mode : str, qid : str) -> list[TrecCovidQrelInstance]:
        if qid not in self.qrel[mode]:
            raise KeyError(f'Qrel for query [{qid}] not found')
        instances = []
        for did, score in self.qrel[mode][qid]:
            instances.append(TrecCovidQrelInstance(qid=qid, did=did, score=score))
        return instances

    def get_qrels(self, mode : str) -> Iterator[TrecCovidQrelInstance]:
        for qid, did, score in self.qrel_list[mode]:
            instance = TrecCovidQrelInstance(qid=qid, did=did, score=score)
            yield instance

    def __str__(self) -> str:
        return 'TrecCovidDataLoader()'

    def __repr__(self) -> str:
        return 'TrecCovidDataLoader()'
