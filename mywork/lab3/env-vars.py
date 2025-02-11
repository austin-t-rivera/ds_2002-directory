#!C:\Users\jason\anaconda3\python.exe

import os
FAVORITE_SPORT = input('what is your favorite sport? ')
PRACTICE_HOURS = input('how many hours do you practice per week? ')
TEAM_PLAYED = input('how many teams do you play on? ')

os.environ["USER_SPORT"] = FAVORITE_SPORT
os.environ["WEEKLY_PRACTICE"] = PRACTICE_HOURS
os.environ["ON_TEAM"] = TEAM_PLAYED

print(os.getenv("USER_SPORT"))
print(os.getenv("WEEKLY_PRACTICE"))
print(os.getenv("ON_TEAM"))

