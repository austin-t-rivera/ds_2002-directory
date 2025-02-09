#! /c/Users/ashle/AppData/Local/Microsoft/WindowsApps/python
import os
os.environ["FAV_FLAVOR"] = "Vanilla"
os.environ["AGE"] = "34"
os.environ["UVA_FIRST_YEAR"] = "True"

DAY_OF_WEEK = input('What is the day of the week today?')
MOOD = input('What is your current mood?')
MONTH = input('What month is it currently?')

os.environ["DAY_OF_WEEK"] = DAY_OF_WEEK
os.environ["MOOD"] = MOOD
os.environ["MONTH"] = MONTH

print(os.getenv("DAY_OF_WEEK"))
print(os.getenv("MOOD"))
print(os.getenv("MONTH"))
