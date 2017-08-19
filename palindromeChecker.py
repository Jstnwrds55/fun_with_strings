def checkIfPalindrome(text):
    listText = list(text)
    reverseText = list(reversed(text))
    if listText == reverseText:
        print(True)
    else:
        print(False)