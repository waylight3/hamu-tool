# hamu-tools
Many useful tools for computer scientists!

Please join our [discord](https://discord.gg/m93jftsr7g) for any help.

## Dataset
### DataLoader
- Full list of available dataset: [HAMU Dataset](http://research.hamu.me/dataset/)

- How to load dataset
```py
from hamu_tool.dataset import DataLoader

loader = DataLoader.load('beir/nfcorpus')

for doc in loader.get_docs():
    print(doc['id'], doc['title'], doc['text'])
    break

for query in loader.get_qeuries():
    print(query['id'], query['text'])
    break

for qrel in loader.get_qrels():
    print(qrel['qid'], qrel['did'], qrel['score'])
    break
```

- How to fetch a document or a query
```py
from hamu_tool.dataset import DataLoader

loader = DataLoader.load('beir/nfcorpus')
doc = loader.get_doc('MED-10')
query = loader.get_query('PLAIN-3')
```

## Utils
### CorpusReader
- How to build and load index
```py
from hamu_tool.utils import CorpusReader

CorpusReader.build_index('data_file.jsonl', 'index_file.idx')
reader = CorpusReader('index_file.idx')
print(reader[0]) # get document by index
print(reader['doc_id']) # get document by id
```
- Format of `data_file.jsonl`: each line of `data_file.jsonl` should be a dictionary
```json
{"id": "doc_1", "text": "doc_text_1"}
```

### BIBExtractor
