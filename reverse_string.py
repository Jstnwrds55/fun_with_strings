print('What string would you like to reverse?')
user_string_input = input()


def reverse_string(user_string):
    new_string = ''
    for x in range(1, len(user_string) + 1):
        new_string += user_string[len(user_string) - x]
    print(new_string)
    return new_string

reverse_string(user_string_input)
