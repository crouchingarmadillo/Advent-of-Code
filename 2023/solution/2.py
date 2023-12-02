# Part One (Time: 00:34:38) (Rank: 7860)
# Input: Games (separated by '\n') with color reveals (separated by ';')
# with cubes (separated by ',') with a color (red, green, blue). 
# Cubes are replaced after each color reveal.
# ex: Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# is the game with id 1 and in the first reveal, 3 blue cubes and 4 red cubes
# are used.

# Output: Compute the sum of the ids of the games possible
# with 12 red cubes, 13 green cubes, and 14 blue cubes.

def possible(line: str) -> bool:
    colors = {"red": 0, "green": 0, "blue": 0}
    reveals = line.split(":")[1].split(";")

    for reveal in reveals:
        cubes = reveal.split(",")
        for cube in cubes:
            num, color = cube.split()
            colors[color] += int(num)
        
        if colors["red"]<=12 and colors["green"]<=13 and colors["blue"]<=14:
            colors["red"] = 0
            colors["green"] = 0
            colors["blue"] = 0
            continue
        else:
            return False
    
    return True

def solution_one(file_name: str) -> str:
    result = 0
    with open(file_name, encoding="utf-8") as f:
        for line in f:
            if possible(line):
                result += int(line.split(":")[0].split()[1])
            else:
                continue
    
    return result

# Part Two (Time: 00:43:39) (Rank: 7730)
# Input: Games (separated by '\n') with color reveals (separated by ';')
# with cubes (separated by ',') with a color (red, green, blue). 
# Cubes are replaced after each color reveal.

# Output: Sum of the powers of games where the power of a game
# is the product of the minimum number of cubes (of each color) you need
# for each game to be possible.
# ex: Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# For this game to be possible we need 4 red, 2 green, and 6 blue.
# So the power is 48 = 4*2*6

def game_power(line: str) -> int:
    colors = {"red": 0, "green": 0, "blue": 0}
    reveals = line.split(":")[1].split(";")
    for reveal in reveals:
        cubes = reveal.split(",")
        for cube in cubes:
            num, color = cube.split()
            if colors[color] < int(num):
                colors[color] = int(num)
            else:
                continue
    
    return colors["red"] * colors["green"] * colors["blue"]

def solution_two(file_name: str) -> str:
    result = 0
    with open(file_name, encoding="utf-8") as f:
        for line in f:
            result += game_power(line)
    
    return result


# Print the answers
if __name__ == "__main__":
    file_name = "../input/2.txt"
    print("solution one: ", solution_one(file_name))
    print("solution two: ", solution_two(file_name))