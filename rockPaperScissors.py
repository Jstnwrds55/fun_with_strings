import random


def playerOptions():
    print('What will you choose, rock(r), paper(p), or scissors(s)')
    playerInput = input()
    while True:
        if playerInput == 's':
            return 'scissors'
        elif playerInput == 'p':
            return 'paper'
        elif playerInput == 'r':
            return 'rock'
        else:
            print('That\'s not an option, silly!')
            continue


def computerChoice():
    rng = random.random()
    if rng <= .33:
        return 'rock'
    elif .33 < rng <= .66:
        return 'paper'
    else:
        return 'scissors'


def isWinner(playerChoice, compChoice):
    if playerChoice == 'scissors':
        if compChoice == 'scissors':
            return 'Tie game!'
        elif compChoice == 'rock':
            return 'Computer wins!'
        else:
            return 'You won!'
    elif playerChoice == 'rock':
        if compChoice == 'scissors':
            return 'You won!'
        elif compChoice == 'rock':
            return 'Tie game!'
        else:
            return 'Computer wins!'
    elif playerChoice == 'paper':
        if compChoice == 'scissors':
            return 'Computer wins!'
        elif compChoice == 'rock':
            return 'You won!'
        else:
            return 'Tie game!'


def main():
    playGame = 'shwaza'
    while playGame == 'shwaza':
        print('Welcome to rock, paper, scissors! Try your hand at beating the computer!')
        player = playerOptions()
        comp = computerChoice()
        print('You chose ' + player + '.')
        print('The computer chose ' + comp + '.')
        print(isWinner(player, comp))
        print('Type shwaza to play again!')
        playGame = input()

main()
