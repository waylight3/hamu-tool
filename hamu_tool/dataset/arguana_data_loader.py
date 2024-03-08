from .data_loader_base import DataLoaderQDRBase

class ArguanaDataLoader(DataLoaderQDRBase):
    def __init__(self):
        super().__init__('beir/arguana')

    def __str__(self) -> str:
        return 'ArguanaDataLoader()'

    def __repr__(self) -> str:
        return 'ArguanaDataLoader()'
