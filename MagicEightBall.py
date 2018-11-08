import random

answers = ['Yes', 'No', 'I believe so', 'I believe not', 'No, you idiot', 'Sure, why not?']

#When app is first ran
print("Hello! \nThis is the 8-Ball from your most wild of dreams. \nWhat is your name?")

name = input()

print(' ')
print('Hello ' + name)



def Magic8Ball():
    print('')
    print("Ask me a question. I promise i'll answer it.")
    input()
    print('')
    print (answers[random.randint(0, len(answers)-1)] )
    Replay()

def Replay():
    print(' ')
    print("Anything else I can help you with, " + name,"?")
    print(" ")
    print("[y/n]")

    # Yes or no
    reply=input()

    if reply == 'y':
        Magic8Ball()
    elif reply == 'n':
        exit()
    else:
        print("What was that?")
        Replay()
        
        
Magic8Ball()


