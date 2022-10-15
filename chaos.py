import random

words=["ironman","hawkeye","thor","wanda","vision","world","chaos","seven","heaven","valorant","pubg","books","mobile","school","code","mother","easy","hello","reading","dispensable" ]
word=random.choice(words)
# print(word)

jumble="".join(random.sample(word,len(word)))
# print(jumble)

chances=3

print("~"*16)
print("~~~ CHAOS ~~~")
print("~"*16)

while chances!=0:
    print("The word is : -",jumble)

    guess=input("Enter your guessed word:- ").lower()

    if guess==word:
        print("Amazing you guessed the word")
        print("you have won")
        print()
        break
    else:
        chances-=1
        print("Oh no thats not the word")
        print("Remeaning chances are :- ",chances)
        print()
else:
    print("All your chances are exhausted")
    print("You Lose")
    print("The correct word is :- ",word)

