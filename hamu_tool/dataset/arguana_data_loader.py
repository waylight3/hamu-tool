from .data_loader_base import DataLoaderQDRBase

class ArguanaDataLoader(DataLoaderQDRBase):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/arguana', *args, **kwargs)

    def __str__(self) -> str:
        return 'ArguanaDataLoader()'

    def __repr__(self) -> str:
        return 'ArguanaDataLoader()'
