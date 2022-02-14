import ssl
import urllib
import urllib.request
import json
import random
from RandomFood import RandomFood
#import everything necesarry for the code to run such as json, random, urllib ect

# This is discouraged but it will avoid certificate validation (prevents error)
ssl._create_default_https_context = ssl._create_unverified_context

foodsURL = "https://random-data-api.com/api/food/random_food"
#url which is used to access the random foods

req = urllib.request.Request(foodsURL)
requestData = json.loads(urllib.request.urlopen(req).read())

food:RandomFood = RandomFood(**requestData)

print (food.ingredient)


Steps = ["""
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
        |               /|\
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
        |               /|\
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
        |               /|\
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
        |               /|\
        |                |
        |               / \
        |
        |
        |
        |
        ___________________
        """]

print(Steps[0])

# Start= input
print(len(food)*" _ ")


def get_input():
    while(True):
        # ask for input
        Start= input(f"Name a letter for this food: ")

        # Input validation
        if(len(Start) != 1):
            print("error 101")
            continue
        if():
         return Start