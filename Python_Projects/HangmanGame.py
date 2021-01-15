import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

guessed = False
words = ["sausage", "unity", "displace", "insurance", "tile", "consumer", "pocket"]
chosenWord = random.choice(words)
blankWord = list("_"*len(chosenWord))
blankWordDisplay = "".join(blankWord)
hangmanStage = 0

while not guessed:
    print(HANGMANPICS[hangmanStage] + "\n")
    print("\n" + blankWordDisplay + "\n")

    if hangmanStage == 6:
        print("You lose!")
        guessed = True
        break

    if "".join(blankWord) == chosenWord:
        print("You win!")
        guessed = True
        break

    guess = input("Guess a letter:")

    if guess in chosenWord:
        wordIndex = chosenWord.index(guess)
        blankWord[wordIndex] = guess
        blankWordDisplay = "".join(blankWord)
    else:
        hangmanStage += 1


