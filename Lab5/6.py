import re
def replace_characters(input_str):
    pattern = re.compile(r'[ ,.]')
    result_str = pattern.sub(':', input_str)
    print(f'{input_str}')
    print(f' {result_str}')
input_string = input()
replace_characters(input_string)