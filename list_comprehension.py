from typing import Sequence


def main():
    """ squares = []
    for i in range(1,101):
        sqr = i**2
        if sqr % 3 != 0:
            squares.append(sqr) """

    squares = [i**2 for i in range(1,101) if i%3 != 0] 

    challenge = [i for i in range(1,100000) if i%4==0 and i%6==0 and i%9==0]

    print(challenge)

main()