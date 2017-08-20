print('What text would you like to use to count the vowels of?')
user_text = input()


def count_vowels(text):
    vowel_amount = 0
    for x in range(0, len(text)):
        if text[x] in 'aeiouAEIOU':
            vowel_amount += 1
    print(vowel_amount)
    return vowel_amount

count_vowels(user_text)