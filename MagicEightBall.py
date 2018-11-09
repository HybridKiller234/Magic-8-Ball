import random

answers = ['Yes', 'No', 'I believe so', 'I believe not', 'No, you idiot', 'Sure, why not?']

#When app is first ran
print("Hello! \nThis is the 8-Ball from your most wild of dreams. \nWhat is your name?")

name = input()

print(' ')
print('Hello ' + name)

def Magic8Ball():
    question = input("\nAsk me a question, I promise i'll answer it!: ")
    if question == '' or question == None:
        print("You gotta tell me something!")
    elif question == 'question':
        print("\nOh I get it. We're doing that. \nLets try again.")
        Magic8Ball()
    else:
        print('')
        print(answers[random.randint(0, len(answers)-1)])
        replay()

def replay():
    question2 = input("\nAnything else I can help you with, %s" % name + "? yes or no: \n")
    if question2 == 'y' or question2 == 'yes':
        Magic8Ball()
    elif question2 == 'n' or question2 == 'no':
        exit()
    else:
        print("What was that?")
        replay()

Magic8Ball()
