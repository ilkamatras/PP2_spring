import re
def match_string(input_str):
    pattern = re.compile(r'ab{2,3}')
    match = pattern.fullmatch(input_str)
    
    if match:
        print(f'The string "{input_str}" matches the string.')
    else:
        print(f'The string "{input_str}" does not match the string.')
input_string = input()
match_string(input_string)