import random
    
happiness = random.randint(1,101)
health = random.randint(1,101)
smarts = random.randint(1,101)
looks = random.randint(1,101)
death_chance= 125
possible_genders = ["male","female", "alien"]
gender= random.choice(possible_genders)
completed_scenarios = []

class Person:
  def __init__(self,name,status,month,grade,gender,popularity,happiness,health,smarts,looks):
    self.name = name
    self.status = status
    self.month = month
    self.grade= grade
    self.gender = gender
    self.popularity = popularity
    self.happiness = happiness
    self.health = health
    self.smarts = smarts 
    self.looks = looks
    
  def introduce(self):
    print(f"Welcome {self.name} to your first day of 9th grade. You were born {self.gender}.")

  def stats(self):
      print(f"Grade: {self.grade} \nMonth: {self.month} \n\n Stats:\n Popularity: {self.popularity} \n Happiness: {self.happiness} \n Health: {self.health} \n Smarts: {self.smarts} \n Looks: {self.looks} \n")
  
  def month_up(self):
    self.month += 1 
    print(f'It is the next month')

  def school_scenarios(self):
    global completed_scenarios
    if self.grade == 9:
      scenario = random.randint(1,3)
      if scenario == 1:
        if 1 not in completed_scenarios:
          completed_scenarios.append(1)
          while True:
            x = input("A bully wants to take your lunch. \n What will you do? \n \n a= punch the bully \n b= give the bully your lunch \n c = run away \n")
            if x == 'a':
              fight = random.randint(1,2)
              if fight == 1:
                print("You got beat up")
                self.health -= 10
                print("OOF that one hurt. Your health just went down ten points")
                break
              if fight == 2:
                print("You won")
                self.happiness += 10
                print("Congrats you surprisingly won! Your happiness went up 10 points")
                break
            elif x == 'b':
              self.happiness -= 10
              print("That one was a blow to your self esteem. Your happiness went down 10 points")
              break
            elif x == 'c':
              self.smarts += 5
              print("Finally, you did something intelligent. Your smarts went up 5 points")
              break
            else:
              print("Error")
      elif scenario == 2:
        if 2 not in completed_scenarios:
          completed_scenarios.append(2)
          while True:
            x = input("You are assigned a group project from your freshman technology teacher. What are you going to do? \n \n a= do all the work \n b= do none of the work \n c= split up the work evenly")
            if x == 'a':
              self.smarts += 10
              print("Congrats try hard. Your now THAT kid, but hey your smarts went up 10 points")
              break
            elif x == 'b':
              self.popularity -= 10
              print("Ew. Now your THAT kid. No one likes you so you lost 10 popularity points")
              break
            elif x == 'c':
              self.popularity += 5
              print("Your chill with your groupmates now. You gained 5 popularity points")
              break
            else:
              print("Error")
      elif scenario == 3:
        if 3 not in completed_scenarios:
          completed_scenarios.append(3)
          while True:
            x = input("Your mom is yelling at you for getting a bad grade in Dr. Gupta's freshman biology class. What is your next move? \n \n a= give up and cry \n b= study harder \n c= bribe the teacher")
            if x == 'a':
              self.happiness -= 10
              print("Since you are a sad, depressed, loser your happiness went down ten points")
              break
            elif x == 'b':
              self.smarts += 10
              print("Wow! Good job! You actually made a good decision. Your smarts went up 10 points")
              break
            elif x == 'c':
              self.smarts -= 10
              print("Nice try! But she failed you and gave you a fat 0. Your smarts went down 10 points.")
              break
            else:
              print("Error")
          
        
        
character = Person(input("What is your name"),"alive",0,9,gender,0,happiness,health,smarts,looks)

character.introduce()

if character.gender == "alien":
  print("⏁⊑⟒ ☌⟟⍀⌰ ⏃⏁ ⏁⊑⟒ ⏚⍜⍜⏁⊑ ⌇⍜⌰⎅ ⎎⟟⎎⏁⊬ ⏚⍜⋏⎅⌇. ⌰⍜⍜☍ ⟟⋏ ⏁⊑⟒ ☊⍜⍀⋏⟒⍀ ⏁⍜ ⎎⟟⋏⎅ ⏁⊑⟒ ⏁⏃⋏ ⌇⊑⟟⍀⏁.⏁⊑⟒ ☌⍀⟒⏃⏁ ⏃⋏⏁⟟⍾⎍⟟⏁⊬ ⍜⎎ ⋏⍜⏁⊑⟟⋏☌ ⟟⌇ ⏃⌿⌿⏃⍀⟒⋏⏁ ⎎⍀⍜⋔ ⟟⏁⌇ ⏚⟒⟟⋏☌ ⌇⍜ ⎐⟟⌇⟟⏚⌰⟒ ⟟⋏ ⏁⊑⟒ ⏃☊☊⍜⎍⋏⏁⌇ ⍙⟒ ⊑⏃⎐⟒ ⍜⎎ ⏁⊑⟒ ⏚⟒☌⟟⋏⋏⟟⋏☌ ⍜⎎ ⟒⎐⟒⍀⊬ ⋏⏃⏁⟟⍜⋏. ⏁⊑⟟⌇ ⟟⌇ ⎐⟒⍀⊬ ⌿⌰⏃⟟⋏⌰⊬ ⏁⍜ ⏚⟒ ⎅⟟⌇☊⍜⎐⟒⍀⟒⎅ ⟟⋏ ⏁⊑⟒ ⎎⟟⍀⌇⏁ ⌿⏃☌⟒⌇, ⏃⋏⎅ ⌇⍜⋔⟒⏁⟟⋔⟒⌇")
  character.status = 'ded'
  print('the fbi found you')
  
while character.status == "alive":
  if character.month == 7:
    character.month = 0
    character.grade += 1
  character.stats()
  death_number = random.randint(1,death_chance)
  kill_number = random.randint(1,death_chance)
  if death_number == kill_number:
    character.staus = "dead"
    print("You died")
    break
  character.school_scenarios()
  print("\n Moves: \n a = advance a month \n")
  while True:
    move = input("What is your next move \n")
    if move == 'a':
      print("\n \n \n \n \n \n \n \n \n \n \n")
      character.month_up()
      break
    else:
      print("Error")
