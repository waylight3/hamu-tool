from .data_loader_base import DataLoaderQDRBase

class SciDocsDataLoader(DataLoaderQDRBase):
    def __init__(self):
        super().__init__('beir/scidocs')

    def __str__(self) -> str:
        return 'SciDocsDataLoader()'

    def __repr__(self) -> str:
        return 'SciDocsDataLoader()'
