from .data_loader_base import DataLoaderQDRBase

class NFCorpusDataLoader(DataLoaderQDRBase):
    def __init__(self):
        super().__init__('nfcorpus')
