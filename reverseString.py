print('What string would you like to reverse?')
userString = input()


def reverseString(userString):
    newString = ''
    for x in range(1, len(userString) + 1):
        newString += userString[len(userString) - x]
    print(newString)
    return newString

reverseString(userString)
