from dataclasses import asdict
from tqdm import tqdm
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
