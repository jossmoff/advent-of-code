import heapq
from collections import Counter

def compute_hand_type(hand):
    occurence_matrix = [[], [], [], [], []]
    jokers = 0
    hand_array = [0 for _ in range(13)]
    most_individual_cards = 0
    for card_num in list(map("J23456789TQKA".index, hand)):
        if card_num != 0:
            hand_array[card_num] += 1
        else:
            jokers += 1
    if jokers == 5:
        return 6
    hand_type = 0
    for idx, count in enumerate(reversed(hand_array)):
        if count != 0:
            most_individual_cards = max(most_individual_cards, count)
            occurence_matrix[count - 1].append(13 - idx)
    if jokers > 0:
        max_element = occurence_matrix[most_individual_cards - 1].pop()
        occurence_matrix[min(4, most_individual_cards - 1 + jokers)].append(max_element)
    if len(occurence_matrix[4]) == 1:
        hand_type = 6
    elif len(occurence_matrix[3]) == 1:
        hand_type = 5
    elif len(occurence_matrix[2]) == 1 and len(occurence_matrix[1]) == 1:
        hand_type = 4
    elif len(occurence_matrix[2]) == 1:
        hand_type = 3
    elif len(occurence_matrix[1]) == 2:
        hand_type = 2
    elif len(occurence_matrix[1]) == 1:
        hand_type = 1
    else:
        hand_type = 0
    return hand_type

def day_7_solution(lines):
    values = []
    for line in lines:
        hand, bid = line.split()
        bid = int(bid)
        hand_type = compute_hand_type(hand)
        hand_value = 0
        for i, digit in enumerate(reversed(list(map("J23456789TQKA".index, hand)))):
            hand_value += digit * (16 ** i)
        values.append((hand_type, hand_value, bid, hand))
    ordered_hands = sorted(values, key=lambda x: (x[0], x[1]))
    winnings = 0
    for rank, (hand_type, hand_value, bid, hand) in enumerate(ordered_hands):
        winnings += (rank + 1) * bid
    return winnings

def test_solution(input_file, expected_value):
    lines = []
    with open(input_file) as f:
        for line in f.readlines():
            lines.append(line.strip())
    val = day_7_solution(lines)
    assert val == expected_value

test_solution('example.input', 5905)
test_solution('tc1.input', 6839)
test_solution('puzzle.input', 253362743)