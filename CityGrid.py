import random
from GridBlock import GridBlock


class CityGrid:
    def __init__(
            self, 
            N: int, 
            M: int, 
            tower_range: int, 
            obstructed_block_coverage: float =0.3
        ) -> None:
        self._grid = [[GridBlock(i, j) for i in range(N)] for j in range(M)]
        self._tower_range = tower_range
        self._surface = N*M
        self._obstructed_blocks_number = int(self._surface * obstructed_block_coverage) + 1
        self._obstructed_blocks_coords = []
        while len(self._obstructed_blocks_coords) < self._obstructed_blocks_number:
            i = random.randint(0, N-1)
            j = random.randint(0, M-1)
            self._grid[j][i].obstruct()
            if (i, j) not in self._obstructed_blocks_coords:
                self._obstructed_blocks_coords.append((i, j))

    def is_full_covered(self) -> bool:
        for row in self._grid:
            for block in row:
                if not block.is_in_cover:
                    return False
        return True

    def place_tower(self, i, j) -> None:
        self._grid[j][i].make_tower()
        for x in range(-self._tower_range, self._tower_range+1):
            for y in range(-self._tower_range, self._tower_range+1):
                if i+x in range(len(self._grid[0])) and j+y in range(len(self._grid)):
                    self._grid[j+y][i+x].cover()

    def fill_towers(self) -> None:
        for x in range(len(self._grid[0])):
            for y in range(len(self._grid)):
                if not self._grid[y][x].is_in_cover and not self._grid[y][x].is_obstructed:
                    try:
                        self.place_tower(x, y)
                    except ValueError:
                        continue
                    

    def __str__(self) -> str:
        return "\n".join(map(str, self._grid))

