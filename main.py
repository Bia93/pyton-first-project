import random

def get_choices():
  player_choice=input('enter a choice :rock,paper,scissors: ')
  computer_choice="paper"
  choices = {"player":player_choice,"computer":computer_choice}
  return choices
choices=get_choices()
print(choices)
#now we ll make it so the computer can actually have a choice
#we are going to learn importing libraries,creating lists and calling methods; usually we put them on the top of the program ex.import random - js- Math.random (random is a library)
#list-array in js- a list in Pyton is used to store multiple items in a single variable
#ex food["pizza","carrots","eggs"]
food["pizza","carrots","eggs"]
dinner=random.choice(food)
print (dinner)

  
