import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    If users give a wrong word, they will loss one chance. They got seven chances to get it right.
    """
    answer = random_word()
    n = N_TURNS
    if_correct_put_ch = dash_at_the_beginning(answer)
    body = ''
    print('The word is ' + dash_at_the_beginning(answer))
    while True:
        if n == 0:
            break
        elif if_correct_put_ch.isalpha():
            break
        if n == N_TURNS:    # first question
            guess = input('Your guess: ')
            guess = guess.upper()  # case insensitive
        else:
            print('Now the word is ' + if_correct_put_ch)   # to avoid showing two answers in console
            guess = input('Guess again: ')  # second and question after
            guess = guess.upper()  # case insensitive
        if guess.isalpha():
            if answer.find(guess) == -1:    # wrong loss 1 chance
                n -= 1
                print('Wrong! You got ' + str(n) + ' chances. Guess it wisely!')
                print(slowly_got_hang(n, body))
            else:   # if user provide right answer
                pass_to_put_ch = ''
                for i in range(len(answer)):
                    if answer[i] == guess:
                        pass_to_put_ch += guess
                    else:
                        pass_to_put_ch += if_correct_put_ch[i]
                if_correct_put_ch = pass_to_put_ch
        else:   # no numbers
            print('Give me alphabet.')
    if n == 0:
        print('You are hang!')
    else:
        print('You made it!')
        print('The answer is ' + answer)


def dash_at_the_beginning(answer):
    ans = ''
    for i in range(len(answer)):
        ans += '_'
    return ans


def slowly_got_hang(n, body):
    if n == 6:
        body += '  |'
    elif n == 5:
        body += '  |\n  O'
    elif n == 4:
        body += '  |\n  O\n /|'
    elif n == 3:
        body += '  |\n  O\n /|\\'
    elif n == 2:
        body += '  |\n  O\n /|\\ \n  |'
    elif n == 1:
        body += '  |\n  O\n /|\\ \n  |  \n /'
    elif n == 0:
        body += '  |\n  O\n /|\\ \n  |  \n / \\'
    return body


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
