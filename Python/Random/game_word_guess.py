from random import randint

def win(guess, word):
    if guess == word:
        print("What...wtf man?! You're not human --'...")
    else:
        print("AHA! LOSER! Next one please, THIS LOSER is done already :* -> ;)")

def word_guessing():
    guess = input("""
    Gues which word I'm thinking...
        0 - Dog
        1 - Cat
        2 - Banana
    Type your guess:
    """)
    word = randint(0, 2)
    win(int(guess), word)

def event_loop():
    play = True
    while(play):
        word_guessing()
        play = input("Wanna try again??(Y/N)")
        if play.lower() == "y":
            play = True
        else:
            play = False

def main():
    event_loop()

if __name__ == '__main__':
    main()