from math import sqrt, floor, ceil, prod

def find_record_start_times(total_time, record):
    discriminant = sqrt(total_time**2 - (4 * record))
    lb = floor((total_time - discriminant) / 2)
    ub = ceil((total_time + discriminant) / 2)
    lb = max(lb, 0)
    return ub - lb - 1

def day_6_solution(lines):
    times = [int(time) for time in lines[0].split()[1:]]
    records = [int(record) for record in lines[1].split()[1:]]
    a = [find_record_start_times(total_time, record) for (total_time, record) in zip(times, records)]
    return prod(a)

def test_solution(input_file, expected_value):
    lines = []
    with open(input_file) as f:
        for line in f.readlines():
            lines.append(line.strip())
    val = day_6_solution(lines)
    print(val)
    assert val == expected_value

test_solution('example.input', 71503)
test_solution('puzzle.input', 288)
