import random
   
happiness = random.randint(1,100)
health = random.randint(1,100)
smarts = random.randint(1,100)
looks = random.randint(1,100)
death_chance= 200
possible_genders = ["male","female","alien"]
gender= random.choice(possible_genders)
completed_scenarios = []
times_studied = []
times_workedout = []

class Person:
  def __init__(self,name,status,month_display,month_total,grade,gender,popularity,happiness,health,smarts,looks):
    self.name = name
    self.status = status
    self.month_display = month_display
    self.month_total = month_total
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
      print(f"Grade: {self.grade} \nMonth: {self.month_display} \n\n Stats:\n Popularity: {self.popularity} \n Happiness: {self.happiness} \n Health: {self.health} \n Smarts: {self.smarts} \n Looks: {self.looks} \n")
  
  def month_up(self):
    self.month_display += 1
    self.month_total += 1
    print(f'It is the next month')

  def school_scenarios(self):
    global completed_scenarios
    
    if self.grade == 9:
      while True:
        scenario = random.randint(1,6)
        if scenario not in completed_scenarios:
          break
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
            x = input("You are assigned a group project from your freshman technology teacher. What are you going to do? \n \n a= do all the work \n b= do none of the work \n c= split up the work evenly \n")
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
              print("You're chill with your groupmates now. You gained 5 popularity points")
              break
            else:
              print("Error")
              
      elif scenario == 3:
        if 3 not in completed_scenarios:
          completed_scenarios.append(3)
          while True:
            x = input("Your mom is yelling at you for getting a bad grade in Dr. Gupta's freshman biology class. What is your next move? \n \n a= give up and cry \n b= study harder \n c= bribe the teacher \n")
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
      elif scenario ==4:
        if 4 not in completed_scenarios:
          completed_scenarios.append(4)
          while True:
            x = input("You are on the way to school and you can't find your idea? What are you going to do? \n \n a= Take the L(OP) \n b= Try to sneak into school without it \n c= run back home \n")
            if x=='a':
              print("Well good job losng your ID bozo. It turns out that during your LOP they gave out free food in the cafeteria. You lost 10 points of happiness")
              self.happiness -=10
              break
            if x=='b':
              print("You got caught trying to sneak into school. Now you have LOP for the whole week. You lost 20 points of happiness")
              self.happiness -=20
              break
            if x =='c':
              print("You found your ID! One problem though you got back to school late, but who really cares about that. Happiness is up 10 points.")
              self.happiness += 10
              break
            else:
              print("Error")
      elif scenario ==5:
        if 5 not in completed_scenarios:
          completed_scenarios.append(5)
          while True:
            x = input("You are in the cafeteria, but you don't see any of your friends. What are you going to do? \n a= eat lunch in the bathroom \n b= make new friends \n c= go talk to a teacher about something \n ")
            if x=='a':
              print("Wow, you really are a loser. Someone saw you eating lunch on the toilet and told the whole school. Popularity down 10 points")
              self.popularity -=10
              break
            if x=='b':
              print("Congrats you were social for once. You actually made some new friends. Popularity up 10 points")
              self.popularity +=10
              break
            if x =='c':
              print("I mean this isn't that sad I guess. Good job for being a good student? Your smarts went up 5 points")
              self.smarts +=5
              break
            else:
              print("Error")
      elif scenario ==6:
        if 6 not in completed_scenarios:
          completed_scenarios.append(6)
          while True:
            x = input("So you are walking down the senior hallway and you see one of them trip you and then look at their friends and laugh. Whats your next move? \n a= run away crying \n b= make fun of the senior \n c= don't say anything and do not make eye contact with anyone for the rest of the year \n") 
            if x=='a':
              print("Are you kidding me? This is the saddest thing ever. Everything is going down 5 points")
              self.health -= 5
              self.happiness -= 5
              self.popularity -= 5
              self.smarts -= 5
              self.looks -= 5
              break
            if x=='b':
              print("You made fun of the senior's ugly haircut causing all his friends to laugh. You gained their respect. Popularity up 10 points")
              self.popularity += 10
              break
            if x =='c':
              print("Um. Ok I guess. This is weird. IDK what to do here so nothing is changing")
              break
            else:
              print("Error")

    elif self.grade == 10:
      while True:
        scenario = random.randint(11,15)
        if scenario not in completed_scenarios:
          break
      if scenario ==11:
        if 11 not in completed_scenarios:
          completed_scenarios.append(11)
          while True:
            x = input("Its time for the AutoCad Exam. Are you ready to take it? \n a = yes \n b= no \n")
            if x=='a':
              print("Congrats! You failed. We both know you were not ready! Your smarts went down 5 points for failing and another 5 points for being cocky.")
              self.smarts -= 10
              break
            if x=='b':
              print("Congrats! You failed, but you knew you were going to so since you know yourself so well your smarts went up 10 points")
              smarts += 10
              break
            else:
              print("Error")
      elif scenario ==12:
        if 12 not in completed_scenarios:
          completed_scenarios.append(12)
          while True:
            x = input("As you were on your way to math class you trip and start falling down the stairs. What are you going to do? \n a= try and catch yourself \n b= let yourself fall")
            if x=='a':
              print("You only fell down three stairs before you caught yourself. Your friends laughed but there was no injury.Nothing happens")
              break
            if x=='b':
              print("Um so you fell down both flights of stairs and got a black eye and bruised ego. Also, someone took a video and sent it to the whole school. Your popularity and looks went down 5 points")
              self.popularity -= 5
              self.looks -= 5
              break
            else:
              print("Error")
      elif scenario ==13:
        if 13 not in completed_scenarios:
          completed_scenarios.append(13)
          while True:
            x = input("So you went really hard in gym class and failed to notice your pit stains developing. It wasn't ")
            if x=='a':
              break
            if x=='b':
              break
            if x =='c':
              break
            else:
              print("Error")
      elif scenario ==14:
        if 14 not in completed_scenarios:
          completed_scenarios.append(14)
          while True:
            x = input("")
            if x=='a':
              break
            if x=='b':
              break
            if x =='c':
              break
            else:
              print("Error")
      elif scenario ==15:
        if 15 not in completed_scenarios:
          completed_scenarios.append(15)
          while True:
            x = input("")
            if x=='a':
              break
            if x=='b':
              break
            if x =='c':
              break
            else:
              print("Error")
              
    elif self.grade == 11:
      while True:
        scenario = random.randint(21,25)
        if scenario not in completed_scenarios:
          break
      if scenario ==21:
        if 21 not in completed_scenarios:
          completed_scenarios.append(21)
          while True:
            x = input("")
            if x=='a':
              break
            if x=='b':
              break
            if x =='c':
              break
            else:
              print("Error")
      elif scenario ==22:
        if 22 not in completed_scenarios:
          completed_scenarios.append(22)
          while True:
            x = input("")
            if x=='a':
              break
            if x=='b':
              break
            if x =='c':
              break
            else:
              print("Error")
      elif scenario ==23:
        if 23 not in completed_scenarios:
          completed_scenarios.append(23)
          while True:
            x = input("")
            if x=='a':
              break
            if x=='b':
              break
            if x =='c':
              break
            else:
              print("Error")
      elif scenario ==24:
        if 24 not in completed_scenarios:
          completed_scenarios.append(24)
          while True:
            x = input("")
            if x=='a':
              break
            if x=='b':
              break
            if x =='c':
              break
            else:
              print("Error")
      elif scenario ==25:
        if 25 not in completed_scenarios:
          completed_scenarios.append(25)
          while True:
            x = input("")
            if x=='a':
              break
            if x=='b':
              break
            if x =='c':
              break
            else:
              print("Error")

    elif self.grade == 12:
      while True:
        scenario = random.randint(31,35)
        if scenario not in completed_scenarios:
          break
      if scenario ==31:
        if 31 not in completed_scenarios:
          completed_scenarios.append(31)
          while True:
            x = input("")
            if x=='a':
              break
            if x=='b':
              break
            if x =='c':
              break
            else:
              print("Error")
      elif scenario ==32:
        if 32 not in completed_scenarios:
          completed_scenarios.append(32)
          while True:
            x = input("")
            if x=='a':
              break
            if x=='b':
              break
            if x =='c':
              break
            else:
              print("Error")
      elif scenario ==33:
        if 33 not in completed_scenarios:
          completed_scenarios.append(33)
          while True:
            x = input("")
            if x=='a':
              break
            if x=='b':
              break
            if x =='c':
              break
            else:
              print("Error")
      elif scenario ==34:
        if 34 not in completed_scenarios:
          completed_scenarios.append(34)
          while True:
            x = input("")
            if x=='a':
              break
            if x=='b':
              break
            if x =='c':
              break
            else:
              print("Error")
      elif scenario ==35:
        if 35 not in completed_scenarios:
          completed_scenarios.append(35)
          while True:
            x = input("")
            if x=='a':
              break
            if x=='b':
              break
            if x =='c':
              break
            else:
              print("Error")


  def study(self):
    if self.month_total in times_studied:
      print("We all know you aint studying more than once a month. Nice try")
    else:
      times_studied.append(self.month_total)
      print('You went to the library to study like a good boy. Your smarts went up 5 points.')
      self.smarts += 5
      
  def workout(self):
    if self.month_total in times_workedout:
      print("You got your swole on so hard you broke the gym. Come back at a later time.")
    else:
      times_workedout.append(self.month_total)
      while True:
        x = input("What are you working on? \n c = cardio \n f = flexibility \n w = weights \n p = pretend to do something \n")
        y = random.randint(1,10)
        if y == 1:
          print("Nice job bozo. You injured yourself at the gym. Your health is now down 10 points.")
          self.health -= 10
          break
        elif x == 'c':
          print("The only other time I have you seen you ran that fast is into Wendy's when you heard they were having a deal. But hey your looks and health went up 5 points")
          self.looks += 5
          self.health += 5
          break
        elif x == 'f':
          print("Maybe next time youll actually be able to touch your toes but at least you put in some effort. Your health went up 5 points")
          self.health += 5
          break
        elif x== 'w':
          print("Damn the grind really is real. You actually broke a sweat. Not gonna lie im surprised. Your looks went up 10 points")
          self.looks += 10
          break
        elif x== 'p':
          print("This is lowkey sad but hey what works for you works for me so your happiness went up 5 points.")
          self.happiness += 5
          break
        else:
          print("Error")
                              
character = Person(input("What is your name"),"alive",1,1,9,gender,50,happiness,health,smarts,looks)

character.introduce()
        
if character.gender == "alien":
  print("⏁⊑⟒ ☌⟟⍀⌰ ⏃⏁ ⏁⊑⟒ ⏚⍜⍜⏁⊑ ⌇⍜⌰⎅ ⎎⟟⎎⏁⊬ ⏚⍜⋏⎅⌇. ⌰⍜⍜☍ ⟟⋏ ⏁⊑⟒ ☊⍜⍀⋏⟒⍀ ⏁⍜ ⎎⟟⋏⎅ ⏁⊑⟒ ⏁⏃⋏ ⌇⊑⟟⍀⏁.⏁⊑⟒ ☌⍀⟒⏃⏁ ⏃⋏⏁⟟⍾⎍⟟⏁⊬ ⍜⎎ ⋏⍜⏁⊑⟟⋏☌ ⟟⌇ ⏃⌿⌿⏃⍀⟒⋏⏁ ⎎⍀⍜⋔ ⟟⏁⌇ ⏚⟒⟟⋏☌ ⌇⍜ ⎐⟟⌇⟟⏚⌰⟒ ⟟⋏ ⏁⊑⟒ ⏃☊☊⍜⎍⋏⏁⌇ ⍙⟒ ⊑⏃⎐⟒ ⍜⎎ ⏁⊑⟒ ⏚⟒☌⟟⋏⋏⟟⋏☌ ⍜⎎ ⟒⎐⟒⍀⊬ ⋏⏃⏁⟟⍜⋏. ⏁⊑⟟⌇ ⟟⌇ ⎐⟒⍀⊬ ⌿⌰⏃⟟⋏⌰⊬ ⏁⍜ ⏚⟒ ⎅⟟⌇☊⍜⎐⟒⍀⟒⎅ ⟟⋏ ⏁⊑⟒ ⎎⟟⍀⌇⏁ ⌿⏃☌⟒⌇, ⏃⋏⎅ ⌇⍜⋔⟒⏁⟟⋔⟒⌇")
  character.status = 'ded'
  print('the fbi found you')
  
while character.status == "alive":
  if character.month_total ==24:
          character.status = 'graduated'
          break
  if character.month_display == 7:
    character.month_display = 1
    character.grade += 1
        
  if character.health < 0:
    character.health = 0
  if character.health > 100:
    character.health = 100
  if character.happiness < 0:
    character.happiness = 0
  if character.happiness > 100:
    character.happiness = 100
  if character.smarts < 0:
    character.smarts = 0
  if character.smarts > 100:
    character.smarts = 100
  if character.looks < 0:
    character.looks = 0
  if character.looks > 100:
    character.looks = 100
    
  character.stats()
  death_number = random.randint(1,death_chance)
  kill_number = random.randint(1,death_chance)
  if character.health == 0 or death_number == kill_number:
    character.status = "dead"
    break
  character.school_scenarios()
  print("\n Moves: \n a = advance a month \n s = go study at the library \n w = go workout")
  while True:
    move = input("What is your next move \n")
    if move == 'a':
      print("\n \n \n \n \n \n \n \n \n \n \n")
      character.month_up()
      break
    elif move == 's':
      character.study()
    elif move == 'w':
      character.workout()
    else:
      print("Error")

while character.status == "dead":
  x = random.randint(1,2)
  if x == 1:
    print("You died of an advil overdose")
    break
  if x == 2:
    print("You tripped and fell and drowned in the toilet. There was no poop in it though so you are all good")
    break
while character.status == 'graduated':
  print("Congrats you have graduated")
  break


##      elif scenario ==36:
##        if 36 not in completed_scenarios:
##          completed_scenarios.append(36)
##          while True:
##            x = input("")
##            if x=='a':
##              break
##            if x=='b':
##              break
##            if x =='c':
##              break
##            else:
##              print("Error")
