print('What sentence would you like to translate to Pig-Latin?')
inputSentence = input()


def pigLatin(userSentence):
    wordList = userSentence.split()
    for x in range(0, len(wordList)):
        if wordList[x] == 'a':
            wordList[x] = 'a-way'
        elif wordList[x][0] in ['a', 'e', 'i', 'o', 'u']:
            wordList[x] += '-way'
        else:
            wordList[x] = wordList[x][1:len(wordList[x])] + '-' + wordList[x][0] + 'ay'
    translatedSentence = ' '.join(wordList)
    print(translatedSentence)
    return translatedSentence

pigLatin(inputSentence)
