print('What sentence would you like to translate to Pig-Latin?')
inputSentence = input()


def pigLatin(userSentence):
    wordList = userSentence.split()
    for x in range(0, len(wordList)):
        lastLetter = wordList[x][len(wordList[x]) - 1]
        try:
            int(wordList[x][0])
            continue
        except:
            pass
        if len(wordList[x]) == 1:
            wordList[x] += '-way'
        elif wordList[x][0] in 'aeiouAEIOU':
            if lastLetter.isalpha():
                wordList[x] += '-way'
            else:
                wordList[x] = wordList[x][0:len(wordList[x]) - 1] + '-way' + lastLetter
        else:
            if lastLetter.isalpha():
                wordList[x] = wordList[x][1:len(wordList[x])] + '-' + wordList[x][0] + 'ay'
            else:
                wordList[x] = wordList[x][1:len(wordList[x]) - 1] + '-' + wordList[x][0] + 'ay' + lastLetter
    translatedSentence = ' '.join(wordList)
    print(translatedSentence)
    return translatedSentence

pigLatin(inputSentence)
