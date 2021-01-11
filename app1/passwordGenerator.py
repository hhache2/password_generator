import random


def getPassword(length, isUppercase, isNumbers, isSpecial):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if isUppercase:
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if isSpecial:
        characters.extend(list('!@#$%^&*()-_+='))

    if isNumbers:
        characters.extend(list('1234567890'))

    thePassword = ''
    for x in range(length):
        thePassword += random.choice(characters)
    return thePassword