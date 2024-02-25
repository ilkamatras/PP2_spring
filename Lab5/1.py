import re
input_string = input()
if re.fullmatch(r'a*b*', input_string):
    print(f'The string "{input_string}" matches the string.')
else:
    print(f'The string "{input_string}" does not match the string.')