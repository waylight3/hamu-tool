from .data_loader_base import DataLoaderQDRBase

class FiQADataLoader(DataLoaderQDRBase):
    def __init__(self):
        super().__init__('fiqa')

    def __str__(self):
        return 'FiQADataLoader()'

    def __repr__(self):
        return 'FiQADataLoader()'
