import random
#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#chosen_word = word_list[random.randint(0,len(word_list)-1)]
chosen_word = random.choice(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Guess a letter\n").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

correct = False

for c in list(chosen_word):
    if c == guess:
        correct = True

print(f"The final word is {chosen_word}")

if correct:
    print(f"You guessed correct: {guess} is in {chosen_word}")
else:
    print(f"You guessed incorrectly: {guess} is not in {chosen_word}")