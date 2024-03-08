from .data_loader_base import DataLoaderQDRBase

class Robust04DataLoader(DataLoaderQDRBase):
    def __init__(self):
        super().__init__('beir/robust04')

    def __str__(self) -> str:
        return 'Robust04DataLoader()'

    def __repr__(self) -> str:
        return 'Robust04DataLoader()'
