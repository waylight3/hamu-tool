from .data_loader_base import DataLoaderQDRBase

class SciDocsDataLoader(DataLoaderQDRBase):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/scidocs', *args, **kwargs)

    def __str__(self) -> str:
        return 'SciDocsDataLoader()'

    def __repr__(self) -> str:
        return 'SciDocsDataLoader()'
