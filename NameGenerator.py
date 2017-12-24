import string 
import random

#inputs from user from which computer will chose a 
LetterInput1 = input(str("Chose a letter... v for vowels, c for consonants. l for any other letters"))
LetterInput2 = input(str("Chose a letter... v for vowels, c for consonants. l for any other letters"))
LetterInput3 = input(str("Chose a letter... v for vowels, c for consonants. l for any other letters"))
LetterInput4 = input(str("Chose a letter... v for vowels, c for consonants. l for any other letters"))
LetterInput5 = input(str("Chose a letter... v for vowels, c for consonants. l for any other letters"))

vowels = "aeiouy"
consonants = "bcdfghjklmnpqrstuvwxz"
letter = string.ascii_lowercase

def generator():
    if LetterInput1 == "v":
        letter1 = random.choice(vowels)
    elif LetterInput1 == "c":
        letter1 = random.choice(consonants)
    elif LetterInput1 == "l":
        letter1 = random.choice(letter)
    else:
        letter1 = LetterInput1

    if LetterInput2 == "v":
        letter2 = random.choice(vowels)
    elif LetterInput2 == "c":
        letter2 = random.choice(consonants)
    elif LetterInput2 == "l":
        letter2 = random.choice(letter)
    else:
        letter2 = LetterInput2

    if LetterInput3 == "v":
        letter3 = random.choice(vowels)
    elif LetterInput3 == "c":
        letter3 = random.choice(consonants)
    elif LetterInput3 == "l":
        letter3 = random.choice(letter)
    else:
        letter3 = LetterInput3

    if LetterInput4 == "v":
        letter4 = random.choice(vowels)
    elif LetterInput4 == "c":
        letter4 = random.choice(consonants)
    elif LetterInput4 == "l":
        letter4 = random.choice(letter)
    else:
        letter4 = LetterInput4

    if LetterInput5 == "v":
        letter5 = random.choice(vowels)
    elif LetterInput5 == "c":
        letter5 = random.choice(consonants)
    elif LetterInput5 == "l":
        letter5 = random.choice(letter)
    else:
        letter5 = LetterInput5

    name = letter1 + letter2 + letter3 + letter4 + letter5
    return name

for babynames in range (10):
    print(generator())
