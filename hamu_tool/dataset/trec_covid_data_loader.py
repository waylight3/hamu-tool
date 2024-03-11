from .data_loader_base import DataLoaderQDRBase

class TrecCovidDataLoader(DataLoaderQDRBase):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/trec-covid', *args, **kwargs)

    def __str__(self) -> str:
        return 'TrecCovidDataLoader()'

    def __repr__(self) -> str:
        return 'TrecCovidDataLoader()'
