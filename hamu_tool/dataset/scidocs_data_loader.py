from .data_loader_base import DataLoaderQDRBase

class SciDocsDataLoader(DataLoaderQDRBase):
    def __init__(self):
        super().__init__('scidocs')
