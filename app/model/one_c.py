import dataclasses


@dataclasses.dataclass
class OneCNomenclature:
    id: int
    name: str
    price: float


@dataclasses.dataclass
class OneCClient:
    id: int
    name: str


def get_nomenclatures() -> list[OneCNomenclature]:
    pass


def get_clients() -> list[OneCClient]:
    pass


def get_nomenclature_by_id(id_) -> OneCNomenclature:
    pass
