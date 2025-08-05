import random

chance=6

stages = [
    """
       ------
       |    |
       |    O
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
    """
]


print("Hi, this is Hangman game written by Joseph")
print("")
print("")
print("The fate of the man who may be hanged on this gallows lies in your hands... " )
print()
print("" \
"""
       ------
       |    |
       |    
       |
       |
       |
       -----
    """)

print()
print("These are the words you should find letter by letter...")
my_list=['station','cap','dog','juice','random','hangman','superman']

print(my_list)
print()
print("Each wrong letter brings him closer to his doom... Can you save him?")
print()
print("If you think that you found the word, type the whole word to win the game early")
print("Entering the same letter again will be a wasted chance")
print()

my_list=['station','cap','dog','juice','random','hangman','superman']

print(my_list)

randomword=random.choice(my_list)

copyrandomword=randomword

count=0

print("Write 'start' to start the game")
print("")
startcommand=input()
print("")
print("You have 6 chances to find the word, please",end=" ")

if startcommand=="start":
    while len(randomword)>0:
        letter = input("enter a letter: ")
        if letter==copyrandomword:
            randomword=""
        elif letter in randomword:
            for i in randomword:
                if letter==i:
                    count=count+1
            print(count,end=" ")
            print("found✅")
            randomword=randomword.replace(letter,'')
        else:
            print(stages[6 - chance])
            chance=chance-1
            print("wrong letter, you have",end=" ")
            print(chance, end=" ")
            print("chances")
            if chance==0:
                break
    if len(randomword)==0:
        print("The word was: '"+copyrandomword+"'")
        print("You won, congratulations!✅")
    else:
        print("You lost❌")
        print("The word was: "+copyrandomword)
        print("Try again")
    
else:
    print("the game couldn't start")