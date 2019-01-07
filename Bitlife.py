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

  def stats(self):
      print(f"Stats:\n Wealth: {self.wealth} \n Happiness: {self.happiness} \n Health: {self.health} \n Smarts: {self.smarts} \n Looks: {self.looks} \n")
  
  def age_up(self):
    self.age += 1 
    print(f'You are now {self.age} years old.')
    
happiness = random.randint(1,101)
health = random.randint(1,101)
smarts = random.randint(1,101)
looks = random.randint(1,101)
death_chance= 125
possible_genders = ["male","female"]
gender= random.choice(possible_genders)

character = Person(input("What is your name"),"alive",0,gender,0,happiness,health,smarts,looks)

character.introduce()

while character.status == "alive":
    character.stats()
    x = death_chance - character.age
    death_number = random.randint(1,x+1)
    kill_number = random.randint(1,x+1)
    if death_number == kill_number:
      character.staus = "dead"
      print("You died")
      break
    print("\n Moves: \n a = grow older a year \n")
    move = input("What is your next move \n")
    if move == 'a':
      for x in range(10):
          print("\n")
      character.age_up()
        
