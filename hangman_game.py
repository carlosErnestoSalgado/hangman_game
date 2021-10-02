import random, os
import time

# Lectura de la base de datos
def read():
    words = []
    
    with open('./files/data.txt', 'r', encoding='UTF-8') as f:
        for line in f:
            words.append(line.strip().upper())
    return words



def main():
    data = read()
    random_word = random.choice(data)
    list_word = [letter for letter in random_word]
    list_spaces = ["_"] * len(list_word)
    dict_of_word = dict(enumerate(random_word))
    
    while list_spaces != list_word:
        try:
            os.system('cls')
            print('Adivina la palabra!')
            for element in list_spaces:
                print(element + ' ', end='')
            print('\n')

            char = input('Entre una letra: ').strip().upper()
            if len(char) > 1 or not char.isalpha():
                raise ValueError('Error!. En la entrada de Datos')
            for key, value in dict_of_word.items():
                if value == char:
                    list_spaces[key] = value

            if '_' not in list_spaces:
                os.system('cls')
                print(f'Felicidades ha ganado! \nLa palabra es {random_word}')
        except ValueError as error:
            os.system('cls')
            print(error)
            time.sleep(3)
            


if __name__=='__main__':
    main()