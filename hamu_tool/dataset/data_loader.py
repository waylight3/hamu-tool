import requests

from .sparse.beir import ArguanaDataLoader
from .sparse.beir import BioASQDataLoader
from .sparse.beir import ClimateFEVERDataLoader
from .sparse.beir import DBPediaDataLoader
from .sparse.beir import FEVERDataLoader
from .sparse.beir import FiQADataLoader
from .sparse.beir import HotpotQADataLoader
from .sparse.beir import MSMARCODataLoader
from .sparse.beir import NFCorpusDataLoader
from .sparse.beir import NQDataLoader
from .sparse.beir import QuoraDataLoader
from .sparse.beir import Robust04DataLoader
from .sparse.beir import SciDocsDataLoader
from .sparse.beir import SciFactDataLoader
from .sparse.beir import Signal1MDataLoader
from .sparse.beir import ToucheDataLoader
from .sparse.beir import Touchev2DataLoader
from .sparse.beir import TrecCovidDataLoader
from .sparse.beir import TrecNewsDataLoader

class DataLoader:
    """DataLoader class to load dataset from the list of available datasets
    """
    def __init__(self):
        pass

    @staticmethod
    def dataset_list() -> list:
        """Fetch the list of available datasets from the server.

        Raises:
            Exception: If failed to fetch the dataset list.

        Returns:
            list: List of available datasets.
        """
        res = requests.get('http://research.hamu.me/dataset/api/get_list/')
        if res.status_code == 200:
            data = res.json()
            dataset_list = data['dataset_list']
            return dataset_list
        else:
            raise Exception('Failed to fetch dataset list')

    @staticmethod
    def load(dataset_name : str, *args, **kwargs) -> any:
        """Load the dataset with the given name.

        Args:
            dataset_name (str): Name of the dataset to load.

        Raises:
            Exception: If the dataset is not found.

        Returns:
            @@DataLoader: The dataset wrapper object.
        """
        dataset_list = DataLoader.dataset_list()
        wrapper_mapping = { dataset['name']: dataset['wrapper'] for dataset in dataset_list }

        if dataset_name in wrapper_mapping:
            wrapper_class = globals()[wrapper_mapping[dataset_name]]
            return wrapper_class(*args, **kwargs)
        else:
            raise Exception(f'Dataset [{dataset_name}] not found')
