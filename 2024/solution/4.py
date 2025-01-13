xmas_list = list("XMAS")
samx_list = list("SAMX")

mas_list = list("MAS")
sam_list = list("SAM")

def horizontal(grid: list[list[str]]) -> int:
    count = 0
    max_y = len(grid)
    max_x = len(grid[0]) - 3
    for y in range(max_y):
        row_y = grid[y]
        for x in range(max_x):
            candidate = row_y[x:x+4]
            if candidate == xmas_list or candidate == samx_list:
                count += 1
            
    return count

def vertical(grid: list[list[str]]) -> int:
    count = 0
    max_y = len(grid) - 3
    max_x = len(grid[0])

    for y in range(max_y):
        for x in range(max_x):
            candidate = [grid[y+i][x] for i in range(4)]
            if candidate == xmas_list or candidate == samx_list:
                count += 1

    return count

def diagonal(grid: list[list[str]]) -> int:
    count = 0
    # Top left -> bottom right
    max_y = len(grid) - 3
    max_x = len(grid[0]) - 3
    for y in range(max_y):
        for x in range(max_x):
            candidate = [grid[y+i][x+i] for i in range(4)]
            if candidate == xmas_list or candidate == samx_list:
                count += 1
        

    # Bottom left -> top right
    for y in range(max_y):
        for x in range(len(grid[0]) - 1, 2, -1):
            candidate = [grid[y+i][x-i] for i in range(4)]
            if candidate == xmas_list or candidate == samx_list:
                count += 1

    return count


def part1(filename: str) -> int:
    grid = []
    with open(filename, "r") as f:
        for line in f:
            grid.append(list(line.rstrip()))

    count = 0
    count += horizontal(grid)
    count += vertical(grid)
    count += diagonal(grid)
    return count

def part2(filename: str) -> int:
    grid = []
    with open(filename, "r") as f:
        for line in f:
            grid.append(list(line.rstrip()))

    count = 0
    max_x = len(grid[0]) - 2
    max_y = len(grid) - 2

    for y in range(max_y):
        for x in range(max_x):
            center = grid[y+1][x+1]
            top_left = grid[y][x]
            top_right = grid[y][x+2]
            bot_left = grid[y+2][x]
            bot_right = grid[y+2][x+2]

            candidate0 = [top_left, center, bot_right]
            candidate1 = [bot_left, center, top_right]

            if (candidate0==mas_list or candidate0==sam_list) and (candidate1==mas_list or candidate1==sam_list):
                count += 1
            
    return count

def main():
    filename = "input/4"
    print(f"part1: {part1(filename)}")
    print(f"part2: {part2(filename)}")

if __name__ == "__main__":
    main()
