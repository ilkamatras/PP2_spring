import re
def match_string(input_str):
    pattern = re.compile(r'a.*b$')
    match = pattern.fullmatch(input_str)
    if match:
        print(f'The string "{input_str}" matches the pattern.')
    else:
        print(f'The string "{input_str}" does not match the pattern.')
input_string = input()
match_string(input_string)