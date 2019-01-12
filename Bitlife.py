import random
class Person:
  def __init__(self,name,status,month,grade,gender,wealth,happiness,health,smarts,looks):
    self.name = name
    self.status = status
    self.month = month
    self.grade= grade
    self.gender = gender
    self.wealth = wealth
    self.happiness = happiness
    self.health = health
    self.smarts = smarts 
    self.looks = looks
    
  def introduce(self):
    print(f"Welcome {self.name} to your first day of 9th grade. You were born {self.gender}.")

  def stats(self):
      print(f"Month: {self.month} \n Stats:\n Wealth: {self.wealth} \n Happiness: {self.happiness} \n Health: {self.health} \n Smarts: {self.smarts} \n Looks: {self.looks} \n")
  
  def month_up(self):
    self.month += 1 
    print(f'It is the next month')

  def school_scenarios(self):
    if self.grade == 9:
      scenario = 1
      if scenario == 1:
        x = input("A bully wants to take your lunch. \n What will you do? \n \n a= punch the bully \n b= give the bully your lunch \n c = run away \n")
        if x == 'a':
          fight = random.randint(1,2)
          if fight == 1:
            print("You got beat up")
            self.health -= 10
          if fight == 2:
            print("You won")
            self.happiness += 10
        if x == 'b':
          self.happiness -= 10
        if x == 'c':
          self.smarts += 5
    
happiness = random.randint(1,101)
health = random.randint(1,101)
smarts = random.randint(1,101)
looks = random.randint(1,101)
death_chance= 125
possible_genders = ["male","female", "alien"]
gender= random.choice(possible_genders)

character = Person(input("What is your name"),"alive",0,9,gender,0,happiness,health,smarts,looks)

character.introduce()

if character.gender == "alien":
  print("⏁⊑⟒ ☌⟟⍀⌰ ⏃⏁ ⏁⊑⟒ ⏚⍜⍜⏁⊑ ⌇⍜⌰⎅ ⎎⟟⎎⏁⊬ ⏚⍜⋏⎅⌇. ⌰⍜⍜☍ ⟟⋏ ⏁⊑⟒ ☊⍜⍀⋏⟒⍀ ⏁⍜ ⎎⟟⋏⎅ ⏁⊑⟒ ⏁⏃⋏ ⌇⊑⟟⍀⏁.⏁⊑⟒ ☌⍀⟒⏃⏁ ⏃⋏⏁⟟⍾⎍⟟⏁⊬ ⍜⎎ ⋏⍜⏁⊑⟟⋏☌ ⟟⌇ ⏃⌿⌿⏃⍀⟒⋏⏁ ⎎⍀⍜⋔ ⟟⏁⌇ ⏚⟒⟟⋏☌ ⌇⍜ ⎐⟟⌇⟟⏚⌰⟒ ⟟⋏ ⏁⊑⟒ ⏃☊☊⍜⎍⋏⏁⌇ ⍙⟒ ⊑⏃⎐⟒ ⍜⎎ ⏁⊑⟒ ⏚⟒☌⟟⋏⋏⟟⋏☌ ⍜⎎ ⟒⎐⟒⍀⊬ ⋏⏃⏁⟟⍜⋏. ⏁⊑⟟⌇ ⟟⌇ ⎐⟒⍀⊬ ⌿⌰⏃⟟⋏⌰⊬ ⏁⍜ ⏚⟒ ⎅⟟⌇☊⍜⎐⟒⍀⟒⎅ ⟟⋏ ⏁⊑⟒ ⎎⟟⍀⌇⏁ ⌿⏃☌⟒⌇, ⏃⋏⎅ ⌇⍜⋔⟒⏁⟟⋔⟒⌇")
  character.status = 'ded'
  print('the fbi found you')
  
while character.status == "alive":
  if character.month == 10:
    character.month = 0
    character.grade += 1
  character.stats()
  death_number = random.randint(1,death_chance)
  kill_number = random.randint(1,death_chance)
  if death_number == kill_number:
    character.staus = "dead"
    print("You died")
    break
  print("\n Moves: \n a = advance a month \n")
  move = input("What is your next move \n")
  if move == 'a':
    print("\n \n \n \n \n \n \n \n \n \n \n")
    character.month_up()


    


      
    
        
