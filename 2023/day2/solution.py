from collections import defaultdict
from math import prod

def parse_game_for_max_cube_counts(game: str):
    max_colours = defaultdict(int)
    configs = game.split(': ')[1]
    shows = configs.split(';')
    for show in shows:
        ball_counts = show.split(', ')
        for ball_count in ball_counts:
            count, colour = ball_count.strip().split(' ')
            max_colours[colour] = max(max_colours[colour], int(count))
    print(max_colours)
    return max_colours

def sum_of_possible_games(max_red_count, max_green_count, max_blue_count, games):
    sum_result = 0
    for game_number, game in enumerate(games): 
        game_max_counts = parse_game_for_max_cube_counts(game)
        if game_max_counts['red'] <= max_red_count and game_max_counts['blue'] <= max_blue_count and game_max_counts['green'] <= max_green_count:
            sum_result += game_number + 1
    return sum_result

def power_of_cubes(game): 
    game_max_counts = parse_game_for_max_cube_counts(game)
    return prod(game_max_counts.values())


lines = []
with open('aoc2.input') as f:
    lines = f.readlines()

print(sum([power_of_cubes(game) for game in lines]))
