from art import *
from game_data import data
import random


position = list(range(0,50))
score = 0
last_correct = 0

def render_data(data_d):
  name  = data_d[0]
  value = data_d[1]
  description = data_d[2]
  place = data_d[3]
  if data_d == a:
    print(f"Compare A: {name}, a {description}, from {place}\n")
    print(vs)
  elif data_d == b:
    print(f"Against B: {name}, a {description}, from {place}")
  return value


def select_person():
  select = position.pop(random.randint(0,len(position)-1))
  return select

def pop_person (arr):
  x = list(arr[select_person()].values())
  return x

end_of_game = False
#WHILE LOOP
while end_of_game == False:
  print(logo)

  if last_correct == 0:
    a = pop_person(data)
    b = pop_person(data)
  elif   last_correct == a:
    b = pop_person(data)
  elif last_correct == b:
    a = b
    b = pop_person(data)
  
  a_value = render_data(a)
  b_value = render_data(b)
  

  if a_value > b_value:
    correct = "A"
    last_correct = a
    
  elif b_value > a_value:
    last_correct = b
    correct = "B"
    

  resp = input("Who has more followers? A or B\n").upper()

  if resp == correct:
    score += 1
    print(f"You´re right! score = {score}")
    if score == 49:
      print("Congratulations you reach the end!!")
      print("Game over")
      end_of_game = True

  else:# resp!= correct:
    print(f"Sorry That´s wrong, final score = {score}")
    end_of_game = True