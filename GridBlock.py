class GridBlock:
    def __init__(self, x, y) -> None:
        self._coords = (x, y)
        self._string = "__"
        self._is_obstructed = False
        self._is_tower = False
        self._is_in_coverage = False

    def obstruct(self) -> None:
        self._is_obstructed = True
        self._string = f"O{self._string[1]}"
        
    def make_tower(self) -> None:
        if not self._is_obstructed and not self._is_tower:
            self._is_tower = True
            self._string = f"T{self._string[1]}"
        else:
            raise ValueError(f"cannot place tower on {self._coords=}")

    def cover(self) -> None:
        self._is_in_coverage = True
        self._string = f"{self._string[0]}*"

    @property
    def is_in_cover(self) -> bool:
        return self._is_in_coverage

    @property
    def is_obstructed(self) -> bool:
        return self._is_obstructed
        
    @property
    def is_tower(self) -> bool:
        return self._is_tower

    def __str__(self) -> str:
        return self._string

    def __repr__(self) -> str:
        return self._string
