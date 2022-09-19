import random
from hangman_art import stages
from hangman_art import logo

print(logo)
life = 6
list_of_words = ["bakary", "bouba","younouss"]
word = random.choice(list_of_words)
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
        print(f"The letter {guess} is not in the word. You have {life}  lives left")
        print(stages[life])
        if life == 0:
            end_of_game = True
            print("you lose")
    if "_" not in blanks:
        end_of_game = True
        print("you win")
