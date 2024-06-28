import requests

from .sparse.beir import BEIRArguanaDataLoader
from .sparse.beir import BEIRBioASQDataLoader
from .sparse.beir import BEIRClimateFEVERDataLoader
from .sparse.beir import BEIRDBPediaDataLoader
from .sparse.beir import BEIRFEVERDataLoader
from .sparse.beir import BEIRFiQADataLoader
from .sparse.beir import BEIRHotpotQADataLoader
from .sparse.beir import BEIRMSMARCODataLoader
from .sparse.beir import BEIRNFCorpusDataLoader
from .sparse.beir import BEIRNQDataLoaderader
from .sparse.beir import BEIRQuoraDataLoader
from .sparse.beir import BEIRRobust04DataLoader
from .sparse.beir import BEIRSciDocsDataLoader
from .sparse.beir import BEIRSciFactDataLoader
from .sparse.beir import BEIRSignal1MDataLoader
from .sparse.beir import BEIRToucheDataLoader
from .sparse.beir import BEIRTouchev2DataLoader
from .sparse.beir import BEIRTrecCovidDataLoader
from .sparse.beir import BEIRTrecNewsDataLoader

from .sparse.gpl import GPLArguanaDataLoader
from .sparse.gpl import GPLBioASQDataLoader
from .sparse.gpl import GPLClimateFEVERDataLoader
from .sparse.gpl import GPLDBPediaDataLoader
from .sparse.gpl import GPLFEVERDataLoader
from .sparse.gpl import GPLFiQADataLoader
from .sparse.gpl import GPLHotpotQADataLoader
from .sparse.gpl import GPLNFCorpusDataLoader
from .sparse.gpl import GPLNQDataLoader
from .sparse.gpl import GPLQuoraDataLoader
from .sparse.gpl import GPLRobust04DataLoader
from .sparse.gpl import GPLSciDocsDataLoader
from .sparse.gpl import GPLSciFactDataLoader
from .sparse.gpl import GPLSignal1MDataLoader
from .sparse.gpl import GPLToucheDataLoader
from .sparse.gpl import GPLTrecCovidDataLoader
from .sparse.gpl import GPLTrecNewsDataLoader

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
