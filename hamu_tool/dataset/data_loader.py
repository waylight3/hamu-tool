from .arguana_data_loader import ArguanaDataLoader
from .fiqa_data_loader import FiQADataLoader
from .nfcorpus_data_loader import NFCorpusDataLoader
from .robust04_data_loader import Robust04DataLoader
from .scidocs_data_loader import SciDocsDataLoader
from .scifact_data_loader import SciFactDataLoader
from .trec_covid_data_loader import TrecCovidDataLoader
from .webis_touche_2020_data_loader import WebisTouche2020DataLoader
import requests

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
    def load(dataset_name : str) -> object:
        """Load the dataset with the given name.

        Args:
            dataset_name (str): Name of the dataset to load.

        Raises:
            Exception: If the dataset is not found.

        Returns:
            object: The dataset wrapper object.
        """
        dataset_list = DataLoader.dataset_list()
        wrapper_mapping = { dataset['name']: dataset['wrapper'] for dataset in dataset_list }

        if dataset_name in wrapper_mapping:
            wrapper_class = globals()[wrapper_mapping[dataset_name]]
            return wrapper_class()
        else:
            raise Exception(f'Dataset [{dataset_name}] not found')