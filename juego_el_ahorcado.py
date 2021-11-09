import random 
import os
from functools import reduce

words = []

def read_words_file():
    with open("./files/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            words.append(line.strip().upper())

def get_word():
    try:
        assert len(words) > 0, "No existen más palabras en el juego"
        return random.choice(words)
    except AssertionError:
        print("Ya no hay más palabras para jugar.")

def validate_word(word, shown, letter):
    for i in range(len(word)):
        if word[i] == letter:
            shown[i] = True

def main():
    try:
        # Prepare words selection
        read_words_file()
        word = get_word()

        shown_letters = [False for i in range(len(word))]
        print(word)

        is_over = reduce(lambda curr, value: curr and value, shown_letters)

        while not is_over:
            os.system("clear")
            status = ""
            for i in range(len(shown_letters)):
                letter = word[i]
                if shown_letters[i]:
                    status += letter + " "
                else:
                    status += "_ "
            print("¡Adivina la palabra!")
            print(status)

            letter = input("\nIngresa una letra: ").strip().upper()
            validate_word(word, shown_letters, letter)
            is_over = reduce(lambda curr, value: curr and value, shown_letters)
        
        os.system("clear")
        print("¡Ganaste!\n\nLa palabra es: {0}".format(word))
        
    except KeyboardInterrupt:
        os.system("clear")
        print("Gracias por jugar. Adiós.")

if __name__=="__main__":
    main()