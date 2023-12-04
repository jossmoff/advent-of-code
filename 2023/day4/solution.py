
def compute_numbers_set_from_string(numbers_string):
    numbers = set()
    for number in numbers_string.split():
        numbers.add(int(number))
    return numbers

def day_4_solution(lines):
    num_cards = len(lines)
    card_counts = [1 for _ in range(num_cards)]
    
    for card_count, line in enumerate(lines):
        if card_counts[card_count] == 0:
            continue
        winning_numbers_string, our_numbers_string = line.split(': ')[1].split(' | ')
        winning_numbers = compute_numbers_set_from_string(winning_numbers_string)
        our_numbers = compute_numbers_set_from_string(our_numbers_string)
        winning_numbers_count = len(winning_numbers & our_numbers)
        if winning_numbers_count > 0:
            for idx in range(1, winning_numbers_count + 1):
                if card_count + idx >= num_cards:
                    continue
                card_counts[card_count + idx] += card_counts[card_count]
    print(card_counts)
    return sum(card_counts)
        

def test_solution(input_file, expected_value):
    lines = []
    with open(input_file) as f:
        for line in f.readlines():
            lines.append(line.strip())
    val = day_4_solution(lines)
    print(val)
    assert val == expected_value

test_solution('example.input', 30)
test_solution('puzzle.input', 13)
