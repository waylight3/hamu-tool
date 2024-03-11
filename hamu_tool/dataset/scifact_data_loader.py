from .data_loader_base import DataLoaderQDRBase

class SciFactDataLoader(DataLoaderQDRBase):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/scifact', *args, **kwargs)

    def __str__(self) -> str:
        return 'SciFactDataLoader()'

    def __repr__(self) -> str:
        return 'SciFactDataLoader()'