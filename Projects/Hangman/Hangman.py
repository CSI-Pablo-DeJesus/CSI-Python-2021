import json
import os
from pathlib import Path
from Food import Food


myPath = Path(__file__).parents[0]
myFilePath = os.path.join(myPath, 'random_food.json')
data = open(myFilePath, 'r')
 

data = json.load(data)
food:Food = Food(**data)


print(f"ID: {food.id}")
print(f"UID: {food.uid}")
print(f"dish: {food.dish}")
print(f"description: {food.description}")
print(f"description: {food.description}")
print(f"ingredient: {food.ingredient}")
print(f"measurement: {food.measurement}")

["""
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
 
 ["""
 |----------------+
 |                |
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
 
 ["""
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
 
 ["""
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
 
 ["""
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
 
 ["""
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
 
 ["""
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
 
 ["""
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
 """,
 """
 
 """]