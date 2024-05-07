from ..utils.corpus_reader import CorpusReader
from dataclasses import asdict
from tqdm import tqdm
import glob
import os
import requests
import shutil
import tempfile
import urllib.parse

class DataLoaderBase:
    """Base class for DataLoader
    """
    def __init__(self, dataset_name : str, force_download : bool = False):
        """Constructor for DataLoaderBase

        Args:
            dataset_name (str): Name of the dataset to load.
            force_download (bool, optional): Whether to force download the dataset. Defaults to False.
        """
        self.dataset_name = dataset_name
        self.download_urls = self._fetch_download_urls(dataset_name)
        self.data_dir = os.path.join(tempfile.gettempdir(), 'hamu_tool', 'dataset', self.dataset_name)
        if os.path.exists(self.data_dir):
            if not force_download:
                return
            shutil.rmtree(self.data_dir)
        os.makedirs(self.data_dir)
        print(f'Downloading dataset [{self.dataset_name}] ...')
        for url in self.download_urls:
            self._download_from_url(url, self.data_dir)

    def _fetch_download_urls(self, dataset_name : str) -> list[str]:
        """Fetch the download urls for the given dataset.

        Args:
            dataset_name (str): Name of the dataset to fetch download urls.

        Raises:
            Exception: If failed to fetch download urls for the dataset.

        Returns:
            list[str]: List of download urls for the dataset.
        """
        res = requests.get(f'http://research.hamu.me/dataset/api/get_download_url/{urllib.parse.quote(dataset_name, safe="")}/')
        if res.status_code == 200:
            data = res.json()
            download_urls = data['download_url'].split('\n')
            if len(download_urls) == 0 or download_urls[0] == '':
                raise Exception(f'No download urls found for the dataset [{dataset_name}]')
            return download_urls
        else:
            raise Exception('Failed to fetch download urls')

    def _download_from_url(self, url : str, data_dir : str) -> None:
        """Download the dataset from the given url.

        Args:
            url (str): URL to download the dataset.
            data_dir (str): Directory to save the downloaded dataset.

        Raises:
            Exception: If failed to download the dataset.
        """
        res = requests.get(url, stream=True)
        if res.status_code == 200:
            filename = res.headers.get('content-disposition').split('filename=')
            if len(filename) > 1:
                filename = filename[1]
            else:
                filename = res.headers.get('content-disposition').split('filename*=')[-1].split("''")[-1]
            total = int(res.headers.get('content-length', 0))
            pbar = tqdm(total=total, desc=filename, unit='B', unit_scale=True, unit_divisor=1024)
            data_path = os.path.join(data_dir, filename)
            with open(data_path, 'wb') as fp:
                for data in res.iter_content(chunk_size=1024):
                    pbar.update(len(data))
                    fp.write(data)
                # fp.write(res.content)
        else:
            raise Exception('Failed to download dataset')

class DataLoaderQDRBase(DataLoaderBase):
    """Base class for DataLoaderQDR
    """
    def __init__(self, dataset_name : str, *args, **kwargs):
        """Constructor for DataLoaderQDRBase

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

    def total_qrels(self, mode : str) -> int:
        """Total number of qrels in the dataset.

        Args:
            mode (str): Mode of the dataset.

        Returns:
            int: Total number of qrels in the dataset.
        """
        return len(self.qrel_list[mode])

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

    def get_qrel(self, mode : str, qid : str):
        """Fetch the qrel instances by query ID.

        Args:
            mode (str): Mode of the dataset.
            qid (str): The query ID.

        Raises:
            KeyError: If qrel for the query ID not found.

        Returns:
            list[QrelInstance]: List of fetched qrel instances.
        """
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

    def get_drel(self, mode : str, did : str):
        """Fetch the drel instances by document ID.

        Args:
            mode (str): Mode of the dataset.
            did (str): The document ID.

        Raises:
            KeyError: If drel for the document ID not found.

        Returns:
            list[QrelInstance]: List of fetched drel instances.
        """
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
