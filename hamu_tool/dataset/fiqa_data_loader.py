from .data_loader_base import DataLoaderQDRBase

class FiQADataLoader(DataLoaderQDRBase):
    def __init__(self):
        super().__init__('beir/fiqa')

    def __str__(self) -> str:
        return 'FiQADataLoader()'

    def __repr__(self) -> str:
        return 'FiQADataLoader()'
