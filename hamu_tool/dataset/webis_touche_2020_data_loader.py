from .data_loader_base import DataLoaderQDRBase

class WebisTouche2020DataLoader(DataLoaderQDRBase):
    def __init__(self, *args, **kwargs):
        super().__init__('beir/webis-touche2020', *args, **kwargs)

    def __str__(self) -> str:
        return 'WebisTouche2020DataLoader()'

    def __repr__(self) -> str:
        return 'WebisTouche2020DataLoader()'
