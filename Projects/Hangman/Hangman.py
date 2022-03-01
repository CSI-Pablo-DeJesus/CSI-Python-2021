from ctypes.wintypes import WORD
from lib2to3.pytree import LeafPattern 
import ssl 
import urllib
import urllib.request
import json
import random
import string
from RandomFood import RandomFood
#import everything necesarry for the code to run such as json, random, urllib ect

# This is discouraged but it will avoid certificate validation (prevents error)
ssl._create_default_https_context = ssl._create_unverified_context

    # len(food.ingredient)
def tempFormat(temp):
  #define variable
  tempFormat=""
  #for loop 
  for i in range(len(temp)):
    #append letter
    tempFormat = tempFormat + f"{temp[i]} "
  #return format
  return tempFormat

def getWord():

    foodsURL = "https://random-data-api.com/api/food/random_food"
    #url which is used to access the random foods

    req = urllib.request.Request(foodsURL)
    requestData = json.loads(urllib.request.urlopen(req).read())
    #requesting data site which has all the variables available for the game
    current_food:food = food(**requestData)
    food:RandomFood = food(**requestData)
    #make array from words in name
    name =current_food.name.split()


        #return first word of the name
    return name[0]



    x=1 #used to keep track of wrong guesses



print (RandomFood)
#print food ingredient 

def get_input():
   
 while(True):
        # ask for input
        while(True): 
            letter = input("Name Letter")
            letter = input("Name Letter").upper()

        # Input validation
            if(len(letter) != 1):
                        print("error 101:only letters are allowed") #print message if charater is not allowed
                        continue
            if():
                    return letter
                
            if((letter)in Incorrect_characters or Incorrect_integers):
                    print("error 101:incorrect letter or character")
                    continue
            if():
                        return letter
           # the past lines used length to find if player used only one letter and used if else logic to make sure the player does not repear used letters or incorrect/unavaileble letters)
           
 
 
     
   #create list with characters not allowed in-game  
Incorrect_integers = ["0","1","2","3","4","5","6","7","8","9"]
Incorrect_characters = ["`","~","!","@","$","%","^","&","*","(",")","-","_","=","+","[","{","]","}","\\","|",";",":",",","<",".",">","/","?"]

def printWord(word):
    
   
    letter = list(string.ascii_lowercase)
    #grab all the lowercase letter in ascii instead of putting them all in a list(- credits to Hermann Bauer and prof Carlos Cobian for this line)
    lettersinword = list(word)
    attemptedletters = [] #array of attempted letters
    
    wrong_letter="_"
    
    temp:str = ""
    for letter in lettersinword:
        if (letter not in lettersinword):
            return wrong_letter #the past three lines used if else logic to grab the results of letters entered
        continue
    if (letter in letter in lettersinword): 
        temp = temp + letter #results for letters entered using tem[]
        
    else:
        
        temp = temp + "_" #if the letter is wrong
        
        print(temp)
        
        
        word = random.choice(foodsURL = "https://random-data-api.com/api/food/random_food")
        return word
    return word.upper() # in the last three lines i grabbed the url from the other function to put into this since it will be necesarry later on

 
        
def get_steps(): 
    def a(getInput):
          def a(getWord): #grabing variables from other functions to use in this one
    
             for letter in lettersinword: #I tried to grab the function in which this en the variable in the net lime come from but  it would still report a problem
                 if(letter in attemptedletters):
                  steps = steps[0]
                 else: 
                     steps = steps[steps_int_variable+1]
                     steps_int_variable = 0
    return steps 
    
    
    while True:
        print(steps[0])
       
        


        
    
       
        
        





#create steps based on characters(be original)
steps = ["""
        |----------------+
        |                |
        |
        |
        |
        |
        |
        |
        |
        |
        ___________________
        """,
        """
        |----------------+
        new_func()                |
        |                O
        |
        |
        |
        |
        |
        |
        |
        ___________________
        """,
        """
        |----------------+
        |                |
        |                O
        |                |
        |
        |
        |
        |
        |
        |
        ___________________
        """,
        """
        |----------------+
        |                |
        |                O
        |               /|
        |
        |
        |
        |
        |
        |
        ___________________
        """,
        """
        |----------------+
        |                |
        |                O
        |               /|\\
        |                
        |
        |
        |
        |
        |
        ___________________
        """,
        """
        |----------------+
        |                |
        |                O
        |               /|\\
        |                |
        |
        |
        |
        |
        |
        ___________________
        """,
        """
        |----------------+
        |                |
        |                O
        |               /|\\
        |                |
        |               /
        |
        |
        |
        |
        ___________________
        """,
        """
        |----------------+
        |                |
        |                O
        |               /|\\
        |                |
        |               / \\
        |
        |
        |
        |
        ___________________
        """]

print(steps[0])

# Start= input
print(len(RandomFood)*" _ ")


