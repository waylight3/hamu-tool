from .data_loader_base import DataLoaderQDRBase

class SciFactDataLoader(DataLoaderQDRBase):
    def __init__(self):
        super().__init__('beir/scifact')

    def __str__(self) -> str:
        return 'SciFactDataLoader()'

    def __repr__(self) -> str:
        return 'SciFactDataLoader()'