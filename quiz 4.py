#

letter = 'A'
def grade(letter):
    if letter == 'A':
        return 4
    elif letter == 'B':
        return 3
    elif letter == 'C':
        return 2

def main():
    grade(letter)

main()


import random
def odds(n):

    number_of_odds = 0

    for k in range(n):
        r = random.randrange(10)

        print (r)

        if (r % 2) == 1:

            number_of_odds = number_of_odds + 1

    return (number_of_odds)

odds(8)
