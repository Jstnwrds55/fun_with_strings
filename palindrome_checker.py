print('What word do you need to check for palindromeism? (I don\'t think that\'s a real word).')
user_text = input()


def check_if_palindrome(text):
    text_stripped = (''.join([i for i in text if i.isalpha()]).lower())
    list_text = list(text_stripped)
    reverse_text = list(reversed(text_stripped))
    if list_text == reverse_text:
        print('Sure thing, that\'s a palindrome!')
        return True
    else:
        print('Nope, that\'s not a palindrome')
        return False

check_if_palindrome(user_text)