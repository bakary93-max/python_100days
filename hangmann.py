import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

life = 6
listswords = ["bakary", "bouba","younouss"]
word = random.choice(listswords)
blanks = list("_" * len(word))

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter please: ").lower()
    print()
    for i in range(len(word)):
        if guess == word[i]:
            blanks[i] = guess
    print(blanks)
    if guess not in word:
        life -= 1
        print(f"erreur il te reste {life} vies")
        if life == 0:
            end_of_game = True
            print("you lose")
    if "_" not in blanks:
        end_of_game = True
        print("you win")
