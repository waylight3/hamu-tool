from .data_loader_base import DataLoaderQDRBase

class SciFactDataLoader(DataLoaderQDRBase):
    def __init__(self):
        super().__init__('scifact')
