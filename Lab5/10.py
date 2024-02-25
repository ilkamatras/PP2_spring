def camel_to_snake(camel_str):
    snake_str = ''.join(['_' + char.lower() if char.isupper() else char for char in camel_str]).lstrip('_')
    print(snake_str)

camel_case_string = input()
camel_to_snake(camel_case_string)