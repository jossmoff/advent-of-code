

from functools import reduce
import math
 
def lcm(numbers):
    return reduce(lambda x, y: x * y // math.gcd(x, y), numbers, 1)

def construct_node_map(lines):
    node_map = {}
    for line in lines:
        node_name, left_right_str = line.split(' = ')
        left_right = left_right_str[1:-1].split(', ')
        node_map[node_name] = tuple(left_right)
    return node_map

def number_of_steps_to_end_node(node, node_map, direction_sequence):
    steps = 0
    current_node = node
    while not current_node.endswith('Z'):
        direction_to_take = direction_sequence[steps % len(direction_sequence)]
        current_node = node_map[current_node][direction_to_take]
        steps += 1
    return steps

def day_8_solution(lines):
    direction_sequence = [0 if direction == 'L' else 1 for direction in lines[0]]
    node_map = construct_node_map(lines[2:])
    start_nodes = list(filter(lambda node: node.endswith('A'), node_map.keys()))
    steps_to_end_nodes = [number_of_steps_to_end_node(node, node_map, direction_sequence) for node in start_nodes]
    return lcm(steps_to_end_nodes)

def test_solution(input_file, expected_value):
    lines = []
    with open(input_file) as f:
        for line in f.readlines():
            lines.append(line.strip())
    val = day_8_solution(lines)
    print(val)
    assert val == expected_value

test_solution('example.input', 6)
test_solution('puzzle.input', 12833235391111)