import time

STRING_DIGIT_MAP = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}


def compute_calibration_value_from_digits(digits: list[str]):
    # Assuming we get at least one digit
    if len(digits) == 1: 
        digit = digits[0]
        return digit * 10 + digit
    left_digit = digits[0]
    right_digit = digits[-1]
    return 10 * left_digit + right_digit

def compute_calibration_value_for_line_pt2(line: str):
    '''
    Ideally you have a proper string matching algorithm in here that scans efficeintly. However, simply just
    comparing characters in order and finding a match and then resetting the buffer to the last character will work.
    This is because there can only ever be one overlapping character in the digits
    '''
    digits = []
    string_digit_check_buffer = ''
    to_check_digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for character in line:
        if character.isdigit():
            digits.append(int(character))
            string_digit_check_buffer = ''
            continue
        string_digit_check_buffer += character
        to_check_digits = [to_check_digit for to_check_digit in to_check_digits if to_check_digit.startswith(string_digit_check_buffer)]

        # Reset check data structures
        if len(to_check_digits) == 0:
            string_digit_check_buffer = character
            to_check_digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        
        if len(to_check_digits) == 1 and to_check_digits[0] == string_digit_check_buffer:
            digits.append(STRING_DIGIT_MAP[string_digit_check_buffer])
            string_digit_check_buffer = character
            to_check_digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    return compute_calibration_value_from_digits(digits)
st = time.time()
lines = []
with open('aoc1.input') as f:
    lines = f.readlines()
val = sum([compute_calibration_value_for_line_pt2(line) for line in lines])
et = time.time()
print(f'PT2 Calibration Value: {val}')
print(f'Elapsed Time: {et-st}')
