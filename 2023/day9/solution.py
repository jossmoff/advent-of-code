from itertools import pairwise

def compute_next_number_in_history(numbers):
    if all(i == numbers[0] for i in numbers):
        return numbers[0]
    number_diffs = [y-x for (x, y) in pairwise(numbers)]
    return numbers[0] - compute_next_number_in_history(number_diffs)


def day_9_solution(history):
    return sum([compute_next_number_in_history(numbers) for numbers in history])

def test_solution(input_file, expected_value):
    lines = []
    with open(input_file) as f:
        for line in f.readlines():
            numbers = [int(number) for number in line.strip().split()]
            lines.append(numbers)
    val = day_9_solution(lines)
    assert val == expected_value


test_solution('example.input', 2)
test_solution('puzzle.input', 913)