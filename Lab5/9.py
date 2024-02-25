import re
def insert_spaces(input_str):
    result_str = re.sub(r'([a-z])([A-Z])', r'\1 \2', input_str)
    print(result_str)
input_string = input()
insert_spaces(input_string)