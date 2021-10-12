


import random


foo = ['Rock', 'Paper', 'Scissors']
computerChoice = random.choice(foo)

UserChoice=input("Choose between Rock, Paper and Scissors ")

if(UserChoice=="Rock" and computerChoice=="Paper"):
  print("youlose")
elif(UserChoice==computerChoice):
  print(f"The computer picked {computerChoice}")



elif(UserChoice=="Rock" and computerChoice=="Scissors"):
     print("youwin")


elif(UserChoice=="Rock" and computerChoice=="Rock"):
     print("tie")


elif(UserChoice=="Paper" and computerChoice=="Paper"):
     print("tie")


elif(UserChoice=="Paper" and computerChoice=="Scissors"):
     print("youlose")


elif(UserChoice=="Scissors" and computerChoice=="Scissors"):
     print("youlose")



else:
  print("you lose")