def pigLatin(userSentence):
    wordList = userSentence.split()
    for x in range(0, len(wordList)):
        if wordList[x] == 'a':
            wordList[x] = 'away'
        elif wordList[x][0] in ['a', 'e', 'i', 'o', 'u']:
            wordList[x] += '-way'
            print(wordList)
        else:
            wordList[x] = wordList[x][1:len(wordList[x])] + '-' + wordList[x][0] + 'ay'
            print(wordList)
    print(wordList)
    return wordList

