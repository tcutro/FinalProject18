import random

import pygame
import random
from pygame.locals import*

happiness = random.randint(25,100)
health = random.randint(25,100)
smarts = random.randint(25,100)
looks = random.randint(25,100)
popularity = random.randint(25,100)
death_chance= 50
possible_genders = ["male","female","alien"]
gender = random.choice(possible_genders)
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
            x = input("As you were on your way to math class you trip and start falling down the stairs. What are you going to do? \n a= try and catch yourself \n b= let yourself fall \n")
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
            x = input("So you went really hard in gym class and failed to notice your pit stains developing. It wasn't until after you changed and put on your school shirt that you saw the dark spots. What is your next move? \n a= ask someone to borrow a shirt \n b= walk around with pit stains \n c= try drying off your shirt with the air dryer \n")
            if x=='a':
              print("One of your friends lends you their shirt but you still smell so your popularity went down 5 points")
              self.popularity += 5
              break
            if x=='b':
              print("Everyone saw your pit stains and tbh thats just nasty. Popularity down 100 points. Theres no way your coming back from that")
              self.popularity -= 100
              break
            if x =='c':
              print("Nice job thinking on your feet. You got the dark spots to go off. Your smarts went up 10 points")
              self.smarts += 10
              break
            else:
              print("Error")
      elif scenario ==14:
        if 14 not in completed_scenarios:
          completed_scenarios.append(14)
          while True:
            x = input("You are walking down the hallway and stop to tie your shoe. A group of annoying freshman than procceed to trample you. What are you doing? \n a = hunt every single one of them down and ... \n b= yell at them \n c= get over yourself \n")
            if x=='a':
              print("Um I am now concerned but the police found out your plans because I informed them and they killed you")
              self.status = "ded"
              break
            if x=='b':
              print("The freshman were so scared of you that they promised never even to look in your direction again. Your happiness went up 5 points")
              self.happiness +=5
              break
            if x =='c':
              print("Bad decision. Never ever let freshman get away with things. Your popularity went down 5 points")
              self.popularity -=5
              break
            else:
              print("Error")
      elif scenario ==15:
        if 15 not in completed_scenarios:
          completed_scenarios.append(15)
          while True:
            x = input("As you are walking into school you fall into the mud and it now looks like you pooped your pants. Whats your next move? \n a= cry and call your mom \n b= run to the bathroom and try to get it off \n c= put on your gym shorts \n")
            if x=='a':
              print("Please stop acting like this its disgusting. Popularity down 5 points")
              self.popularity -=5
              break
            if x=='b':
              print("I mean you did not get the stain out but it ended up looking like a cool design so your popularity and smarts go up 10 points")
              self.popularity +=10
              self.smarts +=10
              break
            if x =='c':
              print("Finally, you made a normal decision. However it is a little cold out so your happiness is down 5 points")
              self.happiness -=5
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
            x = input("Its SAT time. Did you get a tutor? \n a= yes \n b= no \n")
            if x=='a':
              print("Since you got a tutor you actually did not fail congrats. You might actually go to college. Your smarts went up 10 points")
              self.smarts += 10
              break
            if x=='b':
              print("Why in the world did you not get a tutor? Your smarts went down 10 points")
              self.smarts -= 10
              break
            else:
              print("Error")
      elif scenario ==22:
        if 22 not in completed_scenarios:
          completed_scenarios.append(22)
          while True:
            x = input("Its time to meet with your guidance counselor about your future. Have you filled out the college packet? \n a = yes \n b= no \n c= college packet? \n")
            if x=='a':
              print("Good you were actually prepared. Smarts are up 5 points")
              self.smarts += 5
              break
            if x=='b':
              print("Not surprising. Your smarts are down 5 points")
              self.smarts -= 5
              break
            if x =='c':
              print("You should not be at this school. \n Goodbye!")
              self.status = "ded"
              break
            else:
              print("Error")
      elif scenario ==23:
        if 23 not in completed_scenarios:
          completed_scenarios.append(23)
          while True:
            x = input("Its spring break and you have not started your Sanservino timeline yet. Are you going to? \n a= yes \n b= no \n c= I already finished \n")
            if x=='a':
              print("Good thinking. Your smarts went up 10 points")
              self.smarts += 10
              break
            if x=='b':
              print("Honestly don't blame you. The 72 hour challenge is the wave. Your happiness is up 5 points")
              self.hapinness += 10
              break
            if x =='c':
              print("You are the kid no one likes. Your popularity is down 10 points")
              self.popularity -= 10
              break
            else:
              print("Error")
      elif scenario ==24:
        if 24 not in completed_scenarios:
          completed_scenarios.append(24)
          while True:
            x = input("You are working on your favorite project ever. The TECH MIDTERM!!!!! How much do you love it??? \n a= so much \n b= so much \n c= so much \n")
            if x=='a':
              print("YESSSS. Your happiness is up 10 points")
              self.happiness += 10
              break
            if x=='b':
              print("YESSSS. Your happiness is up 10 points")
              self.happiness += 10
              break
            if x =='c':
              print("YESSSS. Your happiness is up 10 points")
              self.happiness += 10
              break
            else:
              print("Error")
      elif scenario ==25:
        if 25 not in completed_scenarios:
          completed_scenarios.append(25)
          while True:
            x = input("Its me. The game. Just wanted to check in and say hi. IK junior year is rough and your probably struggling so here is 10 points in everything. :) Have a good day \n a = accept the gift \n")
            if x=='a':
              self.health += 10
              self.happiness += 10
              self.popularity += 10
              self.smarts += 10
              self.looks += 10
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
            x = input("You are sitting in the senior hallway and a freshman steps on your shoe. What are you going to do? \n a= let it go \n b= yell at the freshman \n c= cry \n")
            if x=='a':
              print("How dare you let a freshman do that. Be ashamed of yourself. Popularity is down 10 points")
              self.popularity -=10
              break
            if x=='b':
              print("Good job. Put them in their place. Everyone applauds you for this. Popularity goes up 20 points")
              self.popularity +=20
              break
            if x =='c':
              print("Why just why? Popularity is down 15 points")
              self.popularity -=15
              break
            else:
              print("Error")
      elif scenario ==32:
        if 32 not in completed_scenarios:
          completed_scenarios.append(32)
          while True:
            x = input("You get up to go to the bathroom and when you come back your phone is gone. What are you gonna do? \n a= scream at everyone \n b= use find my iphone \n c= pretend you don't notice. \n")
            if x=='a':
              print("Ok Calm Down. You will survive. But everyone gets scared and they give you your phone back, but still weird. Popularity is down 5 points")
              self.popularity -= 5
              break
            if x=='b':
              print("Whoever stole your phone is 5 steps ahead of you because they turned it off. Nice try. Smarts are now down 10 points.")
              self.smarts -= 10
              break
            if x =='c':
              print("Smart move. The person who took your phone got bored so they gave it back to you. Smarts are up 10 points.")
              self.smarts += 10
              break
            else:
              print("Error")
      elif scenario ==33:
        if 33 not in completed_scenarios:
          completed_scenarios.append(33)
          while True:
            x = input("You are going to the bathroom and try to flush. Oh no. You clogged the toilet. What's your next move? \n a= tell the janitor \n b= pretend it never happened \n c= flush again  \n")
            if x=='a':
              print("Someone heard you tell the janitor. Now the whole school knows. Popularity is down 10 points")
              self.popularity -= 10
              break
            if x=='b':
              print("I do not blame you. I did not see anything so nothing happens.")
            if x== 'c':
              print("Well that was stupid. When has that ever worked. You flood the school. Smarts are down 5 points")
              self.smarts += 10
              break
            else:
              print("Error")
      elif scenario ==34:
        if 34 not in completed_scenarios:
          completed_scenarios.append(34)
          while True:
            x = input("You are in a rush because you are late to school and accidently door ding the principal. What are you going to do? \n a= move your car \n b= tell the principal \n c= hope he does not notice")
            if x=='a':
              print("Um nice try bozo there are cameras and they saw the whole thing. You got a month of detention. Happiness is down 10 points")
              self.happiness -= 10              
              break
            if x=='b':
              print("He respected you for telling him but still got angry. You got detention for the week. Your happiness is down 5 points")
              self.happiness -= 5
              break
            if x =='c':
              print("So you got really really lucky and he had no clue. Good job I guess. You did not really do anything but you seem like you have no friends so here is 5 points of popularity")
              self.popularity += 5
              break
            else:
              print("Error")
      elif scenario ==35:
        if 35 not in completed_scenarios:
          completed_scenarios.append(35)
          while True:
            x = input("It is college time people. So what college do you want to apply to? \n a= MIT \n b= Rutgers \n c= UCC \n")
            if x=='a':
              print("Nice try dummy. You did not get in. Guess you are living in a cardboard box the rest of your life. Happiness is down 30 points")
              self.happiness -= 30
              break
            if x=='b':
              print("Good choice. You can commute but still have that campus experience. Your happiness is up 10 points")
              self.happiness +=10 
              break
            if x =='c':
              print("Go owls! You just saved your bank balance. Your happiness is up 10 points")
              self.happiness += 10
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
  def stats_constraints(self):
    if self.health < 0:
      self.health = 0
    if self.health > 100:
      self.health = 100
    if self.happiness < 0:
      self.happiness = 0
    if self.happiness > 100:
      self.happiness = 100
    if self.smarts < 0:
      self.smarts = 0
    if self.smarts > 100:
      self.smarts = 100
    if self.looks < 0:
      self.looks = 0
    if self.looks > 100:
      self.looks = 100

  def grade_up(self):
    if self.month_display == 6:
      self.month_display = 1
      self.grade += 1

  def moves(self):
    while True:
      print("\n Moves: \n a = advance a month \n s = go study at the library \n w = go workout")
      move = input("What is your next move \n")
      if move == 'a':
        print("\n \n \n \n \n \n \n \n \n \n \n")
        self.month_up()
        break
      elif move == 's':
        self.study()
      elif move == 'w':
        self.workout()
      else:
        print("Error")

  def dead(self):
    death_number = random.randint(1,death_chance)
    kill_number = random.randint(1,death_chance)
    if self.health == 0 or death_number == kill_number:
      self.status = "dead"
    
  def death(self):
    while self.status == "dead":
      x = random.randint(1,2)
      if x == 1:
        print("You died of an advil overdose \n Game Over")
        break
      if x == 2:
        print("You tripped and fell and drowned in the toilet. There was no poop in it though so you are all good. \n Game Over")
        break
  def graduate(self):
    while self.status == 'graduated':
      print("Congrats you have graduated. \n You won!")
      break
  def graphics(self):
    pygame.init
    pygame.font.init()

    background_color = (255,255,255)
    (width, height) = (500, 800)

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Bit Life Graphics")
    screen.fill(background_color)
            
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(0, 10, 500, -200), 70)
    pygame.draw.rect(screen, (40, 116, 166), pygame.Rect(0, 500, 500, 0), 100)
    pygame.draw.rect(screen, (40, 116, 166), pygame.Rect(0, 500, 500, 0), 100)

    pygame.draw.rect(screen, (234, 242, 248), pygame.Rect(195, 585, 290, 25), 0)

    pygame.draw.rect(screen, (234, 242, 248), pygame.Rect(195, 625, 290, 25), 0)

    pygame.draw.rect(screen, (234, 242, 248), pygame.Rect(195, 665, 290, 25), 0)

    pygame.draw.rect(screen, (234, 242, 248), pygame.Rect(195, 707, 290, 25), 0)

    pygame.draw.rect(screen, (235, 237, 239), pygame.Rect(0, 46, 500, 45), 0)

    pygame.draw.circle(screen, (253, 254, 254), [30, 23], 16, 2)
    pygame.draw.line(screen, (253, 254, 254), [25,26], [35,26], 2)
    pygame.draw.line(screen, (253, 254, 254), [25,22], [35,22], 2)

    pygame.draw.line(screen, (144, 148, 151), [195,570], [195,745], 2)

    pygame.draw.line(screen, (253, 254, 254), [25,18], [35,18], 2)

    pygame.draw.circle(screen, (46, 204, 113), [245, 500], 60, 0)
    pygame.draw.circle(screen, (253, 254, 254), [245, 500], 58, 5)

    pygame.draw.line(screen, (253, 254, 254), [245,470], [245,500], 5)
    pygame.draw.line(screen, (253, 254, 254), [225,485], [265,485], 5)

    pygame.draw.line(screen, (93, 109, 126), [90,450], [90,550], 2)

    pygame.draw.line(screen, (93, 109, 126), [180,450], [180,550], 2)

    pygame.draw.line(screen, (93, 109, 126), [400,450], [400,550], 2)

    pygame.draw.line(screen, (93, 109, 126), [310,450], [310,550], 2)

    pygame.draw.line(screen, (28, 40, 51), [0,90], [500,90], 1)

    max_health = 100
    current_health = self.looks
    percentage = current_health/max_health

    if current_health > 31:
        col = (46, 204, 113)
    elif current_health > 13:
        col = (255, 111, 0)
    else:
        col = (178, 34, 34)
            
    pygame.draw.rect(screen, col, pygame.Rect(197, 707, 290*percentage, 25), 0)

    percentage2 = int(current_health/max_health * 100)
    myfont = pygame.font.SysFont('Chunkfive', 28)
    textsurface = myfont.render(str(percentage2), False, (255,255,255))
    screen.blit(textsurface,(195, 707, 290*percentage, 25))

    max_health = 100
    current_health = self.smarts
    percentage = current_health/max_health

    if current_health > 31:
        col = (46, 204, 113)
    elif current_health > 13:
        col = (255, 111, 0)
    else:
        col = (178, 34, 34)
        
    pygame.draw.rect(screen, col, pygame.Rect(197, 665, 290*percentage, 25), 0)

    percentage2 = int(current_health/max_health * 100)
    myfont = pygame.font.SysFont('Chunkfive', 28)
    textsurface = myfont.render(str(percentage2), False, (255,255,255))
    screen.blit(textsurface,(197, 665, 290*percentage, 25))

    max_health = 100
    current_health = self.health
    percentage = current_health/max_health

    if current_health > 31:
        col = (46, 204, 113)
    elif current_health > 13:
        col = (255, 111, 0)
    else:
        col = (178, 34, 34)

    pygame.draw.rect(screen, col, pygame.Rect(197, 625, 290*percentage, 25), 0)

    percentage2 = int(current_health/max_health * 100)
    myfont = pygame.font.SysFont('Chunkfive', 28)
    textsurface = myfont.render(str(percentage2), False, (255,255,255))
    screen.blit(textsurface,(197, 625, 290*percentage, 25))

    max_health = 100
    current_health = self.happiness
    percentage = current_health/max_health

    if current_health > 31:
        col = (46, 204, 113)
    elif current_health > 13:
        col = (255, 111, 0)
    else:
        col = (178, 34, 34)

    pygame.draw.rect(screen, col, pygame.Rect(197, 585, 290*percentage, 25), 0)

    percentage2 = int(current_health/max_health * 100)
    myfont = pygame.font.SysFont('Chunkfive', 28)
    textsurface = myfont.render(str(percentage2), False, (255,255,255))
    screen.blit(textsurface,(197, 585, 290*percentage, 25))

    myfont = pygame.font.SysFont('Chunkfive', 40)
    textsurface = myfont.render('BitSkool', False, (255, 255, 0))
    screen.blit(textsurface,(200,10))

    myfont = pygame.font.SysFont('Chunkfive', 35)
    textsurface = myfont.render('Happiness', False, (144, 148, 151))
    screen.blit(textsurface,(45,585))

    myfont = pygame.font.SysFont('Chunkfive', 35)
    textsurface = myfont.render('Health', False, (144, 148, 151))
    screen.blit(textsurface,(93,625))

    myfont = pygame.font.SysFont('Chunkfive', 35)
    textsurface = myfont.render('Smarts', False, (144, 148, 151))
    screen.blit(textsurface,(83,665))

    myfont = pygame.font.SysFont('Chunkfive', 35)
    textsurface = myfont.render('Looks', False, (144, 148, 151))
    screen.blit(textsurface,(100,705))

    myfont = pygame.font.SysFont('Chunkfive', 35)
    textsurface = myfont.render('Month', False, (253, 254, 254))
    screen.blit(textsurface,(210,510))

    myfont = pygame.font.SysFont('Chunkfive', 28)
    textsurface = myfont.render(str(popularity), False, (40, 116, 166))
    screen.blit(textsurface,(475,50))

    myfont = pygame.font.SysFont('Chunkfive', 25)
    textsurface = myfont.render('Popularity', False, (40, 116, 166))
    screen.blit(textsurface,(410,70))

    myfont = pygame.font.SysFont('Chunkfive', 25)
    textsurface = myfont.render('Magnet', False, (255, 255, 255))
    screen.blit(textsurface,(20,520))

    myfont = pygame.font.SysFont('Chunkfive', 20)
    textsurface = myfont.render('PowerSchool', False, (255, 255, 255))
    screen.blit(textsurface,(95,523))

    myfont = pygame.font.SysFont('Chunkfive', 25)
    textsurface = myfont.render('Outlook', False, (255, 255, 255))
    screen.blit(textsurface,(323,520))

    myfont = pygame.font.SysFont('Chunkfive', 20)
    textsurface = myfont.render('Google', False, (255, 255, 255))
    screen.blit(textsurface,(430,518))

    myfont = pygame.font.SysFont('Chunkfive', 20)
    textsurface = myfont.render('Classroom', False, (255, 255, 255))
    screen.blit(textsurface,(420,530))


    smile = pygame.transform.scale(pygame.image.load("Untitled.PNG"), [25,25])
    screen.blit(smile,(170,583))
    
    heart = pygame.transform.scale(pygame.image.load("Untitled 2.PNG"), [25,25])
    screen.blit(heart,(170,623))

    brain = pygame.transform.scale(pygame.image.load("Untitled 3.PNG"), [25,25])
    screen.blit(brain,(169,663))

    weather = pygame.transform.scale(pygame.image.load("Untitled 4.PNG"), [25,25])
    screen.blit(weather,(169,703))

    school = pygame.transform.scale(pygame.image.load("cutmypic.PNG"), [45,45])
    screen.blit(school,(25,470))

    mhs = pygame.transform.scale(pygame.image.load("mhs.PNG"), [40,40])
    screen.blit(mhs,(150,3))

    powerschool = pygame.transform.scale(pygame.image.load("powerschool.PNG"), [45,45])
    screen.blit(powerschool,(115,470))

    outlook = pygame.transform.scale(pygame.image.load("outlook.PNG"), [45,45])
    screen.blit(outlook,(335,470))

    gc = pygame.transform.scale(pygame.image.load("gc.PNG"), [45,45])
    screen.blit(gc,(430,470))


    alien = pygame.transform.scale(pygame.image.load("alien.PNG"), [40,40])
    

    girl = pygame.transform.scale(pygame.image.load("girl.PNG"), [40,40])
    

    boy = pygame.transform.scale(pygame.image.load("boy.PNG"), [40,40])
    
    if self.gender == "alien":
      screen.blit(alien,(15,48))
    elif self.gender == "female":
      screen.blit(girl,(15,48))
    elif self.gender == "male":
      screen.blit(boy,(15,48))

            
    pygame.display.flip()


character = Person(input("What is your name"),"alive",1,1,9,gender,50,happiness,health,smarts,looks)
character.graphics()
character.introduce()
        
if character.gender == "alien":
  print("⏁⊑⟒ ☌⟟⍀⌰ ⏃⏁ ⏁⊑⟒ ⏚⍜⍜⏁⊑ ⌇⍜⌰⎅ ⎎⟟⎎⏁⊬ ⏚⍜⋏⎅⌇. ⌰⍜⍜☍ ⟟⋏ ⏁⊑⟒ ☊⍜⍀⋏⟒⍀ ⏁⍜ ⎎⟟⋏⎅ ⏁⊑⟒ ⏁⏃⋏ ⌇⊑⟟⍀⏁.⏁⊑⟒ ☌⍀⟒⏃⏁ ⏃⋏⏁⟟⍾⎍⟟⏁⊬ ⍜⎎ ⋏⍜⏁⊑⟟⋏☌ ⟟⌇ ⏃⌿⌿⏃⍀⟒⋏⏁ ⎎⍀⍜⋔ ⟟⏁⌇ ⏚⟒⟟⋏☌ ⌇⍜ ⎐⟟⌇⟟⏚⌰⟒ ⟟⋏ ⏁⊑⟒ ⏃☊☊⍜⎍⋏⏁⌇ ⍙⟒ ⊑⏃⎐⟒ ⍜⎎ ⏁⊑⟒ ⏚⟒☌⟟⋏⋏⟟⋏☌ ⍜⎎ ⟒⎐⟒⍀⊬ ⋏⏃⏁⟟⍜⋏. ⏁⊑⟟⌇ ⟟⌇ ⎐⟒⍀⊬ ⌿⌰⏃⟟⋏⌰⊬ ⏁⍜ ⏚⟒ ⎅⟟⌇☊⍜⎐⟒⍀⟒⎅ ⟟⋏ ⏁⊑⟒ ⎎⟟⍀⌇⏁ ⌿⏃☌⟒⌇, ⏃⋏⎅ ⌇⍜⋔⟒⏁⟟⋔⟒⌇")
  character.status = 'ded'
  print('the fbi found you')
  
while character.status == "alive":
  character.graphics()
  if character.month_total ==21:
          character.status = 'graduated'
          break
        
  character.grade_up()
        
  character.stats_constraints()
    
  character.stats()

  character.dead()
  
  character.school_scenarios()
  character.graphics()
  if character.status == "ded":
    break
  
  character.moves()
  character.graphics()
  character.death()


character.graduate()
