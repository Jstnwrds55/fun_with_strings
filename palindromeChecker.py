print('What word do you need to check for palindromeism? (I don\'t think that\'s a real word).')
userText = input()


def checkIfPalindrome(text):
    textStripped = (''.join([i for i in text if i.isalpha()]).lower())
    listText = list(textStripped)
    reverseText = list(reversed(textStripped))
    if listText == reverseText:
        print('Sure thing, that\'s a palindrome!')
        return True
    else:
        print('Nope, that\'s not a palindrome')
        return False

checkIfPalindrome(userText)