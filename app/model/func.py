def round_size(value: float, _r: int = 1) -> int or float:
    return round(value, _r) if value - int(value) else int(value)