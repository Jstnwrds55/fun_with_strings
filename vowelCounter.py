print('What text would you like to use to count the vowels of?')
userText = input()


def countVowels(text):
    vowelAmount = 0
    for x in range(0, len(text)):
        if text[x] in 'aeiouAEIOU':
            vowelAmount += 1
    print(vowelAmount)
    return vowelAmount

countVowels(userText)