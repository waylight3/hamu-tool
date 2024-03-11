from .data_loader_base import DataLoaderQDRBase

class Robust04DataLoader(DataLoaderQDRBase):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/robust04', *args, **kwargs)

    def __str__(self) -> str:
        return 'Robust04DataLoader()'

    def __repr__(self) -> str:
        return 'Robust04DataLoader()'
