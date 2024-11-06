import string
from sys import argv


letters = string.ascii_lowercase


def main() -> None: #main has to garantee 0<n<26 antes de chamar as funções,ou pode resultar em erro
    text = input('Normal text:\n').lower() #works no matter the input the user gives, even inputs like '', '1999', '.'.
    print(f'ROT{int(argv[1]):02d}:')
    print(cipher(int(argv[1]), text))
    

def cipher(n =  13, s = '') -> str:
    new_s = ''
    for letter in s:
        if letter in letters:
            index = letters.index(letter)
            #Calls a funtion to retrieve the new letter
            new_letter = rotate(n, index)
            #Add the new letter in place of the old one
            new_s = new_s + new_letter
        else:
            #Add the caractere in the same place in the string, if it's not a letter
            new_s = new_s + letter
    return new_s


def rotate(n = 13, i = 0) -> str:   #n é um valor de 0 a 26
    if (n + i) < 26:
        return letters[n + i]
    else:
        return letters[n + i - 26]


if __name__ == '__main__':
    main()