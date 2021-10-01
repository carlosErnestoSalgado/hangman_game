import random, os

# Lectura de la base de datos
def read():
    palabras = []
    with open('./files/data.txt', 'r', encoding='UTF-8') as f:
        for line in f:
            palabras.append(line)
    return palabras



def main():
    index = random.randint(1, len(read())) # obtengo palabra random
    word = read()[index]                   # guardo la palabra
    spaces = '_'*(len(word)-1)             # creo los espacios para la palabra
    word_index = dict(enumerate(word))     # utilizo la fi=uncion enumerate() que recibe como parametro un iterable
    word_index.popitem()                   # elimino el ultimo par clave:valor del diccionario que es un  \n 
    spaces = dict(enumerate(spaces))

    error = 0                               # Creo un contador 
    good = 0                                # Contador
    while word_index != spaces:
        print(error)
        char = input('Entre una letra: ')
        assert not char.isnumeric(), 'Debe entrar solo letras'
        for key, value in word_index.items():
            if value == char:
                spaces[key] = value
                list = [value for value in spaces.values()]
                act = " ".join(list)
                os.system('cls')
                print('Adivine!')
                print(act)
                good += 1
            else:
                # No acert
                error += 1
        if word_index == spaces:
            print(f'Adivinaste, la palabra es: {word}')
            print(f'Total de entradas: {good+error}')
            print(f'Errores:  {error}')
            


if __name__=='__main__':
    main()