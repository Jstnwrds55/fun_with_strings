print('What sentence would you like to translate to Pig-Latin?')
input_sentence = input()


def pig_latin(userSentence):
    word_list = userSentence.split()
    for x in range(0, len(word_list)):
        last_letter = word_list[x][len(word_list[x]) - 1]
        try:
            int(word_list[x][0])
            continue
        except:
            pass
        if len(word_list[x]) == 1:
            word_list[x] += '-way'
        elif word_list[x][0] in 'aeiouAEIOU':
            if last_letter.isalpha():
                word_list[x] += '-way'
            else:
                word_list[x] = word_list[x][0:len(word_list[x]) - 1] + '-way' + last_letter
        else:
            if last_letter.isalpha():
                word_list[x] = word_list[x][1:len(word_list[x])] + '-' + word_list[x][0] + 'ay'
            else:
                word_list[x] = word_list[x][1:len(word_list[x]) - 1] + '-' + word_list[x][0] + 'ay' + last_letter
    translated_sentence = ' '.join(word_list)
    print(translated_sentence)
    return translated_sentence

pig_latin(input_sentence)
