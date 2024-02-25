def snake_to_camel(snake_str):
    camel_str = ''.join(word.capitalize() for word in snake_str.split('_'))
    print(camel_str)

snake_case_string = input()
snake_to_camel(snake_case_string)