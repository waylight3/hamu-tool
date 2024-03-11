from .data_loader_base import DataLoaderQDRBase

class NFCorpusDataLoader(DataLoaderQDRBase):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/nfcorpus', *args, **kwargs)

    def __str__(self) -> str:
        return 'NFCorpusDataLoader()'

    def __repr__(self) -> str:
        return 'NFCorpusDataLoader()'
