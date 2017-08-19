print('What word do you need to check for palindromeism? (I don\'t think that\'s a real word).')
userText = input()


def checkIfPalindrome(text):
    textStripped = (''.join([i for i in text if i.isalpha()]).lower())
    listText = list(textStripped)
    reverseText = list(reversed(textStripped))
    if listText == reverseText:
        print(True)
    else:
        print(False)

checkIfPalindrome(userText)