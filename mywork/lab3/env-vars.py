#!C:\Users\mikai\anaconda3\envs\datascience\python.exe
import os

fav_food = input('What is your favorite food? ')
fav_sport = input('What is your favorite sport? ')
fav_season = input('What is your favorite season? ')

os.environ["FAV_FOOD"] = fav_food
os.environ["FAV_SPORT"] = fav_sport
os.environ["FAV_SEASON"] = fav_season

print(os.getenv("FAV_FOOD"))
print(os.getenv("FAV_SPORT"))
print(os.getenv("FAV_SEASON"))