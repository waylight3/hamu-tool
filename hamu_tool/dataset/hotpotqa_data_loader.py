from .data_loader_base import DataLoaderQDRBase
from dataclasses import dataclass
from typing import Iterator

@dataclass
class HotpotQAQueryInstance:
    id : str
    text : str

@dataclass
class HotpotQADocInstance:
    id : str
    text : str
    title : str
    url : str

@dataclass
class HotpotQAQrelInstance:
    qid : str
    did : str
    score : int

class HotpotQADataLoader(DataLoaderQDRBase):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/hotpotqa', *args, **kwargs)

    def get_query(self, qid : str | int) -> HotpotQAQueryInstance:
        query = self.reader_query[qid]
        instance = HotpotQAQueryInstance(id=query['id'], text=query['text'])
        return instance

    def get_queries(self) -> Iterator[HotpotQAQueryInstance]:
        for query in self.reader_query:
            instance = HotpotQAQueryInstance(id=query['id'], text=query['text'])
            yield instance

    def get_doc(self, did : str | int) -> HotpotQADocInstance:
        doc = self.reader_doc[did]
        instance = HotpotQADocInstance(id=doc['id'], text=doc['text'], title=doc['title'], url=doc['url'])
        return instance

    def get_docs(self) -> Iterator[HotpotQADocInstance]:
        for doc in self.reader_doc:
            instance = HotpotQADocInstance(id=doc['id'], text=doc['text'], title=doc['title'], url=doc['url'])
            yield instance

    def get_qrel(self, mode : str, qid : str) -> list[HotpotQAQrelInstance]:
        if qid not in self.qrel[mode]:
            raise KeyError(f'Qrel for query [{qid}] not found')
        instances = []
        for did, score in self.qrel[mode][qid]:
            instances.append(HotpotQAQrelInstance(qid=qid, did=did, score=score))
        return instances

    def get_qrels(self, mode : str) -> Iterator[HotpotQAQrelInstance]:
        for qid, did, score in self.qrel_list[mode]:
            instance = HotpotQAQrelInstance(qid=qid, did=did, score=score)
            yield instance

    def __str__(self) -> str:
        return 'HotpotQADataLoader()'

    def __repr__(self) -> str:
        return 'HotpotQADataLoader()'
