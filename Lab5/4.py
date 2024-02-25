import re
def find_sequences(input_str):
    pattern = re.compile(r'[A-Z][a-z]+')
    matches = pattern.findall(input_str)

    if matches:
        print(f'Sequences found')
    else:
        print('No sequences found.')

input_string = input()
find_sequences(input_string)