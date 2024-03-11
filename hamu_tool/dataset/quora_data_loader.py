from .data_loader_base import DataLoaderQDRBase

class QuoraDataLoader(DataLoaderQDRBase):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/quora', *args, **kwargs)

    def __str__(self) -> str:
        return 'QuoraDataLoader()'

    def __repr__(self) -> str:
        return 'QuoraDataLoader()'
