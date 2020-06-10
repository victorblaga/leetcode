from typing import List

directions = ['up', 'down', 'left', 'right']


def is_part_of_grid(new_cell, grid):
    row_idx, col_idx = new_cell
    if row_idx < 0 or col_idx < 0:
        return False
    return row_idx < len(grid) and col_idx < len(grid[row_idx])


def move(cell, direction):
    row_idx, col_idx = cell
    if direction == "up":
        return row_idx - 1, col_idx
    elif direction == "down":
        return row_idx + 1, col_idx
    elif direction == "right":
        return row_idx, col_idx + 1
    elif direction == "left":
        return row_idx, col_idx - 1


def perform_search(land_cell, grid, seen=None):
    result = []
    if seen is None:
        seen = set()

    for direction in directions:
        new_cell = move(land_cell, direction)
        if is_part_of_grid(new_cell, grid) and new_cell not in seen:
            seen.add(new_cell)
            i, j = new_cell
            if grid[i][j] == "1":
                result.append(new_cell)
                result.extend(perform_search(new_cell, grid, seen))

    return result


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        land_cells = set()
        for i in range(len(grid)):
            row = grid[i]
            for j in range(len(row)):
                cell_val = grid[i][j]
                if cell_val == "1":
                    land_cells.add((i, j))

        island_count = 0
        while len(land_cells) > 0:
            land_cell = land_cells.pop()
            island_count += 1
            seen = {land_cell}
            adjacent_lands = perform_search(land_cell, grid, seen)
            for cell in adjacent_lands:
                land_cells.remove(cell)

        return island_count


if __name__ == '__main__':
    # grid = [[1, 1, 1, 1, 0],
    #         [1, 1, 0, 1, 0],
    #         [1, 1, 0, 0, 0],
    #         [0, 0, 0, 0, 0]]
    grid = [[1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1]]
    print(Solution().numIslands(grid))