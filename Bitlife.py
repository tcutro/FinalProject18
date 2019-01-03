import random
class Person:
  def __init__(self,name,status,age,gender,wealth,happiness,health,smarts,looks):
    self.name = name
    self.status = status
    self.age = age
    self.gender = gender
    self.wealth = wealth
    self.happiness = happiness
    self.health = health
    self.smarts = smarts 
    self.looks = looks
    
  def introduce(self):
    print(f"I was born {self.gender}. My name is {self.name}.")
  
  def age_up(self):
    self.age += 1 
    print(f'You are now {self.age} years old.')

character = Person(input("What is your name"),"alive",0,"male",0,40,45,56,78)

print(character.introduce())

while character.status == "alive":
    print("\n Moves: \n a = grow older a year \n")
    move = input("What is your next move \n")
    if move == 'a':
        character.age_up()
