import os
from datetime import datetime

current_datetime = datetime.now()

day = current_datetime.day
year = current_datetime.year

year_directory = os.path.join(os.getcwd(), str(year))
day_directory = os.path.join(year_directory, f'day{day}')

if not os.path.exists(year_directory):
    os.makedirs(year_directory)
if not os.path.exists(day_directory):
    os.makedirs(day_directory)

file_path = os.path.join(day_directory, "solution.py")

contents = f'''
def day_{day}_solution(lines):
    pass

def test_solution(input_file, expected_value):
    lines = []
    with open(input_file) as f:
        for line in f.readlines():
            lines.append(line.strip())
    val = day_{day}_solution(lines)
    assert val == expected_value
'''
with open(file_path, 'w') as f:
    f.write(contents)