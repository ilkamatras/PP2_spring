def split_at_uppercase(input_str):
    current_word = ''
    for char in input_str:
        if char.isupper():
            if current_word:
                print(current_word)
                current_word = char
            else:
                current_word = char
        else:
            current_word += char
    
    if current_word:
        print(current_word)

input_string = input()
split_at_uppercase(input_string)