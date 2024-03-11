from ..utils.corpus_reader import CorpusReader
from typing import Iterator
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
        res = requests.get(url)
        if res.status_code == 200:
            filename = res.headers.get('content-disposition').split('filename=')
            if len(filename) > 1:
                filename = filename[1]
            else:
                filename = res.headers.get('content-disposition').split('filename*=')[-1].split("''")[-1]
            data_path = os.path.join(data_dir, filename)
            with open(data_path, 'wb') as fp:
                fp.write(res.content)
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
        qrel_paths = glob.glob(f'{self.data_dir}/qrel.*.tsv')
        for qrel_path in qrel_paths:
            mode = qrel_path.split('.')[-2]
            self.qrel[mode] = {}
            self.qrel_list[mode] = []
            with open(qrel_path, 'r', encoding='utf-8') as fp:
                for line in fp:
                    qid, _, did, score = line.strip().split()
                    if qid not in self.qrel[mode]:
                        self.qrel[mode][qid] = []
                    self.qrel[mode][qid].append((did, int(score)))
                    self.qrel_list[mode].append((qid, did, int(score)))

    def get_doc(self, did : str | int) -> str:
        """Fetch a document by its ID.

        Args:
            did (str | int): The ID (str) or index (int) of the document.

        Returns:
            str: The fetched document.
        """
        return self.reader_doc[did]

    def get_docs(self) -> Iterator[dict[str, str]]:
        """Iterator for documents in the dataset.

        Yields:
            Iterator[dict[str, str]]: Iterator for documents in the dataset.
        """
        for it in self.reader_doc:
            yield it

    def get_query(self, qid : str | int) -> str:
        """Fetch a query by its ID.

        Args:
            qid (str | int): The ID (str) or index (int) of the query.

        Returns:
            str: The fetched query.
        """
        return self.reader_query[qid]

    def get_queries(self) -> Iterator[dict[str, str]]:
        """Iterator for queries in the dataset.

        Yields:
            Iterator[dict[str, str]]: Iterator for queries in the dataset.
        """
        for it in self.reader_query:
            yield it

    def get_qrel(self, qid : str, mode : str, with_score : bool = False) -> list[str] | list[tuple[str, int]]:
        """Fetch the qrel for the given query ID.

        Args:
            qid (str): The ID of the query.
            mode (str): The mode of the qrel such as 'train', 'dev', or 'test'. Check the document for each dataset.
            with_score (bool, optional): Whether to include the score in the qrel. Defaults to False.

        Raises:
            Exception: If qrel for the given query ID is not found.

        Returns:
            list[str]: When with_score is False. List of relevant document IDs for the query.
            list[tuple[str, int]]: When with_score is True. List of relevant document IDs and their scores for the query.
        """
        if qid not in self.qrel[mode]:
            raise Exception(f'Qrel for query [{qid}] not found')
        if with_score:
            return self.qrel[mode][qid]
        return [did for did, _ in self.qrel[mode][qid]]

    def get_qrels(self, mode : str) -> Iterator[dict[str, any]]:
        """Iterator for qrels in the dataset.

        Args:
            mode (str): The mode of the qrel such as 'train', 'dev', or 'test'. Check the document for each dataset.

        Yields:
            Iterator[dict[str, any]]: Iterator for qrels in the dataset.
        """
        for qid, did, score in self.qrel_list[mode]:
            yield {'qid': qid, 'did': did, 'score': score}
