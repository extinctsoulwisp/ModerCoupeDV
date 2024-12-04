import dataclasses


@dataclasses.dataclass
class OneCNomenclature:
    id: str
    name: str
    price: float
    unit: str


@dataclasses.dataclass
class OneCClient:
    id: str
    name: str


def get_nomenclatures() -> list[OneCNomenclature]:
    pass


def get_clients() -> list[OneCClient]:
    pass


def get_nomenclature_by_id(id_) -> OneCNomenclature:
    pass
