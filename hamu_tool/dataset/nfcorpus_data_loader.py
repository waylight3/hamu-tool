from .data_loader_base import DataLoaderQDRBase
from dataclasses import dataclass
from typing import Iterator

@dataclass
class NFCorpusQueryInstance:
    id : str
    text : str
    url : str

@dataclass
class NFCorpusDocInstance:
    id : str
    text : str
    title : str
    url : str

@dataclass
class NFCorpusQrelInstance:
    qid : str
    did : str
    score : int

class NFCorpusDataLoader(DataLoaderQDRBase):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/nfcorpus', *args, **kwargs)

    def get_query(self, qid : str | int) -> NFCorpusQueryInstance:
        query = self.reader_query[qid]
        instance = NFCorpusQueryInstance(id=query['id'], text=query['text'], url=query['url'])
        return instance

    def get_queries(self) -> Iterator[NFCorpusQueryInstance]:
        for query in self.reader_query:
            instance = NFCorpusQueryInstance(id=query['id'], text=query['text'], url=query['url'])
            yield instance

    def get_doc(self, did : str | int) -> NFCorpusDocInstance:
        doc = self.reader_doc[did]
        instance = NFCorpusDocInstance(id=doc['id'], text=doc['text'], title=doc['title'], url=doc['url'])
        return instance

    def get_docs(self) -> Iterator[NFCorpusDocInstance]:
        for doc in self.reader_doc:
            instance = NFCorpusDocInstance(id=doc['id'], text=doc['text'], title=doc['title'], url=doc['url'])
            yield instance

    def get_qrel(self, qid : str, mode : str) -> list[NFCorpusQrelInstance]:
        if qid not in self.qrel[mode]:
            raise KeyError(f'Qrel for query [{qid}] not found')
        instances = []
        for did, score in self.qrel[mode][qid]:
            instances.append(NFCorpusQrelInstance(qid=qid, did=did, score=score))
        return instances

    def get_qrels(self, mode : str) -> Iterator[NFCorpusQrelInstance]:
        for qid, did, score in self.qrel_list[mode]:
            instance = NFCorpusQrelInstance(qid=qid, did=did, score=score)
            yield instance

    def __str__(self) -> str:
        return 'NFCorpusDataLoader()'

    def __repr__(self) -> str:
        return 'NFCorpusDataLoader()'
