import glob
import json
from dataclasses import asdict
from ....utils import CorpusReader
from ...data_loader_base import DataLoaderBase

class GPLDataLoader(DataLoaderBase):
    """Base class for GPL DataLoaders
    """
    def __init__(self, dataset_name : str, *args, **kwargs):
        """Constructor for GPLDataLoader

        Args:
            dataset_name (str): Name of the dataset to load.
        """
        super().__init__(dataset_name, *args, **kwargs)
        self.reader_doc = CorpusReader(f'{self.data_dir}/doc.idx')
        self.reader_query = CorpusReader(f'{self.data_dir}/query.idx')
        self.qrel = {}
        self.qrel_list = {}
        self.drel = {}
        self.qid_list = {}
        self.did_list = {}
        qrel_paths = glob.glob(f'{self.data_dir}/qrel.*.tsv')
        for qrel_path in qrel_paths:
            mode = qrel_path.split('.')[-2]
            self.qrel[mode] = {}
            self.qrel_list[mode] = []
            self.drel[mode] = {}
            self.qid_list[mode] = []
            self.qid_set = set()
            self.did_list[mode] = []
            self.did_set = set()
            with open(qrel_path, 'r', encoding='utf-8') as fp:
                for line in fp:
                    qid, _, did, score = line.strip().split()
                    if qid not in self.qrel[mode]:
                        self.qrel[mode][qid] = []
                    self.qrel[mode][qid].append((did, int(score)))
                    self.qrel_list[mode].append((qid, did, int(score)))
                    if did not in self.drel[mode]:
                        self.drel[mode][did] = []
                    self.drel[mode][did].append((qid, int(score)))
                    if qid not in self.qid_set:
                        self.qid_set.add(qid)
                        self.qid_list[mode].append(qid)
                    if did not in self.did_set:
                        self.did_set.add(did)
                        self.did_list[mode].append(did)
        self.hneg = {}
        self.hneg_list = []
        hneg_paths = glob.glob(f'{self.data_dir}/hneg.*.jsonl')
        for hneg_path in hneg_paths:
            model = hneg_path.split('.')[-2]
            self.hneg[model] = {}
            self.hneg_list[model] = []
            with open(hneg_path, 'r', encoding='utf-8') as fp:
                for line in fp:
                    data = json.loads(line)
                    self.hneg[model][data['qid']] = data['hneg']
                    self.hneg[model].append((data['qid'], data['hneg']))
        self.triple = {}
        triple_paths = glob.glob(f'{self.data_dir}/triple.*.tsv')
        for triple_path in triple_paths:
            mode = triple_path.split('.')[-2]
            self.triple[mode] = []
            with open(triple_path, 'r', encoding='utf-8') as fp:
                for line in fp:
                    qid, pos, neg, score = line.strip().split()
                    score = float(score)
                    self.triple[mode].append((qid, pos, neg, score))

    def total_docs(self, mode : str = None) -> int:
        """Total number of documents in the dataset.

        Args:
            mode (str, optional): Mode of the dataset. Defaults to None.

        Returns:
            int: Total number of documents in the dataset.
        """
        if not mode:
            size = len(self.reader_doc)
        else:
            size = len(self.did_list[mode])
        return size

    def total_queries(self, mode : str = None) -> int:
        """Total number of queries in the dataset.

        Args:
            mode (str, optional): Mode of the dataset. Defaults to None.

        Returns:
            int: Total number of queries in the dataset.
        """
        if not mode:
            size = len(self.reader_query)
        else:
            size = len(self.qid_list[mode])
        return size

    def total_qrels(self, mode : str) -> int:
        """Total number of qrels in the dataset.

        Args:
            mode (str): Mode of the dataset.

        Returns:
            int: Total number of qrels in the dataset.
        """
        return len(self.qrel_list[mode])

    def total_hnegs(self, model : str) -> int:
        """Total number of hard negatives in the dataset.

        Args:
            model (str): The model name.

        Returns:
            int: Total number of hard negatives in the dataset.
        """
        return len(self.hneg_list[model])

    def total_triples(self, mode : str) -> int:
        """Total number of triples in the dataset.

        Args:
            mode (str): Mode of the dataset.

        Returns:
            int: Total number of triples in the dataset.
        """
        return len(self.triple[mode])

    def get_did(self, idx : int, mode : str = None) -> str:
        """Fetch the document ID by its index.

        Args:
            idx (int): The index of the document.
            mode (str, optional): Mode of the dataset. Defaults to None.

        Returns:
            str: The fetched document ID.
        """
        if not mode:
            did = self.reader_doc.idx_list[idx]
        else:
            did = self.did_list[mode][idx]
        return did

    def get_qid(self, idx : int, mode : str = None) -> str:
        """Fetch the query ID by its index.

        Args:
            idx (int): The index of the query.

        Returns:
            str: The fetched query ID.
        """
        if not mode:
            qid = self.reader_query.idx_list[idx]
        else:
            qid = self.qid_list[mode][idx]
        return qid

    def make_query_instance(self, **kwargs):
        """Make a query instance.

        Args:
            **kwargs: Keyword arguments for the query instance.

        Returns:
            QueryInstance: The query instance dataclass.
        """
        raise NotImplementedError

    def make_doc_instance(self, **kwargs):
        """Make a document instance.

        Args:
            **kwargs: Keyword arguments for the document instance.

        Returns:
            DocInstance: The document instance dataclass.
        """
        raise NotImplementedError

    def make_qrel_instance(self, **kwargs):
        """Make a qrel instance.

        Args:
            **kwargs: Keyword arguments for the qrel instance.

        Returns:
            QrelInstance: The qrel instance dataclass.
        """
        raise NotImplementedError

    def make_hneg_instance(self, **kwargs):
        """Make a hard negative instance.

        Args:
            **kwargs: Keyword arguments for the hard negative instance.

        Returns:
            HnegInstance: The hard negative instance dataclass.
        """
        raise NotImplementedError

    def make_triple_instance(self, **kwargs):
        """Make a triple instance.

        Args:
            **kwargs: Keyword arguments for the triple instance.

        Returns:
            TripleInstance: The triple instance dataclass.
        """
        raise NotImplementedError

    def get_query(self, qid : str | int, mode : str = None):
        """Fetch the query instance by its ID.

        Args:
            qid (str | int): The query ID or index.
            mode (str, optional): Mode of the dataset. Defaults to None.

        Returns:
            QueryInstance: The fetched query instance.
        """
        if isinstance(qid, int):
            qid = self.get_qid(qid, mode)
        query = self.reader_query[qid]
        instance = self.make_query_instance(**asdict(query))
        return instance

    def get_queries(self, mode : str = None):
        """Fetch all query instances.

        Args:
            mode (str, optional): Mode of the dataset. Defaults to None.

        Yields:
            QueryInstance: The fetched query instance.
        """
        if not mode:
            for query in self.reader_query:
                instance = self.make_query_instance(**asdict(query))
                yield instance
        else:
            for qid in self.qid_list[mode]:
                query = self.reader_query[qid]
                instance = self.make_query_instance(**asdict(query))
                yield instance

    def get_doc(self, did : str | int, mode : str = None):
        """Fetch the document instance by its ID.

        Args:
            did (str | int): The document ID or index.
            mode (str, optional): Mode of the dataset. Defaults to None.

        Returns:
            DocInstance: The fetched document instance.
        """
        if isinstance(did, int):
            did = self.get_did(did, mode)
        doc = self.reader_doc[did]
        instance = self.make_doc_instance(**asdict(doc))
        return instance

    def get_docs(self, mode : str = None):
        """Fetch all document instances.

        Args:
            mode (str, optional): Mode of the dataset. Defaults to None.

        Yields:
            DocInstance: The fetched document instance.
        """
        if not mode:
            for doc in self.reader_doc:
                instance = self.make_doc_instance(**asdict(doc))
                yield instance
        else:
            for did in self.did_list[mode]:
                doc = self.reader_doc[did]
                instance = self.make_doc_instance(**asdict(doc))
                yield instance

    def get_qrel(self, qid : str | int, mode : str):
        """Fetch the qrel instances by query ID.

        Args:
            qid (str | int): The query ID or index.
            mode (str): Mode of the dataset.

        Raises:
            KeyError: If qrel for the query ID not found.

        Returns:
            list[QrelInstance]: List of fetched qrel instances.
        """
        if isinstance(qid, int):
            qid = self.get_qid(qid, mode)
        if qid not in self.qrel[mode]:
            raise KeyError(f'Qrel for query [{qid}] not found')
        instances = []
        for did, score in self.qrel[mode][qid]:
            instances.append(self.make_qrel_instance(qid=qid, did=did, score=score))
        return instances

    def get_qrels(self, mode : str):
        """Fetch all qrel instances.

        Args:
            mode (str): Mode of the dataset.

        Yields:
            QrelInstance: The fetched qrel instance.
        """
        for qid, did, score in self.qrel_list[mode]:
            instance = self.make_qrel_instance(qid=qid, did=did, score=score)
            yield instance

    def get_drel(self, did : str | int, mode : str):
        """Fetch the drel instances by document ID.

        Args:
            did (str): The document ID or index.
            mode (str): Mode of the dataset.

        Raises:
            KeyError: If drel for the document ID not found.

        Returns:
            list[QrelInstance]: List of fetched drel instances.
        """
        if isinstance(did, int):
            did = self.get_did(did, mode)
        if did not in self.drel[mode]:
            raise KeyError(f'Drel for document [{did}] not found')
        instances = []
        for qid, score in self.drel[mode][did]:
            instances.append(self.make_qrel_instance(qid=qid, did=did, score=score))
        return instances

    def get_drels(self, mode : str):
        """Fetch all drel instances.

        Args:
            mode (str): Mode of the dataset.

        Returns:
            list[QrelInstance]: List of fetched drel instances.
        """
        return self.get_qrels(mode)

    def get_hneg(self, qid : str | int, model : str):
        """Fetch the hard negatives by query ID.

        Args:
            qid (str | int): The query ID or index.
            model (str): The model name.

        Returns:
            list[str]: List of hard negatives.
        """
        if isinstance(qid, int):
            qid = self.get_qid(qid)
        instances = []
        for did in self.hneg[model][qid]:
            instances.append(self.make_hneg_instance(qid=qid, did=did))
        return instances

    def get_triples(self, mode : str):
        """Fetch all triples.

        Args:
            mode (str): Mode of the dataset.

        Yields:
            tuple[str, str, str, str]: The fetched triple.
        """
        for qid, pos, neg, score in self.triple[mode]:
            instance = self.make_triple_instance(qid=qid, pos=pos, neg=neg, score=score)
            yield instance
