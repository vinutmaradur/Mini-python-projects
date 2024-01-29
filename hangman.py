import random

#words = ["UMBRELLA","COMPUTER","TELESCOPE","SMARTPHONE"]

f = open("words.txt","r")
data = f.readline()
words = data.split()
word = random.choice(words)
word = word.upper()

total_chances = 7
guessed_word = "-"*len(word)

while total_chances != 0 :
    print(guessed_word)
    letter = input("Guess a letter: ").upper()
    if letter in word:
        for index in range(len(word)):
            if word[index] == letter:
                guessed_word = guessed_word[:index] + letter + guessed_word[index+1:]
                

        if guessed_word  == word:
            print("Congratulations you won !!! ") 
            break

    else:
        total_chances -= 1
        print("Incorrect guess")
        print("Remaining chances are : ", total_chances)

else:
    print("Game over")
    print("You lose")
    print("All chances are exhausted")
print("The correct word is ", word)