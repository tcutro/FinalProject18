#imports all neccessary tools
import pygame
import random
from pygame.locals import*

#randomly generates stats to start out each game
happiness = random.randint(25,100)
health = random.randint(25,100)
smarts = random.randint(25,100)
looks = random.randint(25,100)
popularity = random.randint(25,100)

#gives a number that determines the probability of if you randomly die
death_chance= 50

#randomly assigns a gender
possible_genders = ["male","female","alien"]
gender = random.choice(possible_genders)

#List to keep track of what scenarios are completed so that they do not get repeated
completed_scenarios = []

#lists to keep track of if the person did a certain function 
times_studied = []
times_workedout = []

#creates a class for the character in the game
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
    
  #introduces the character
  def introduce(self):
    print(f"Welcome {self.name} to your first day of 9th grade. You were born {self.gender}.")

  
  #makes it so you move a month forward in the game
  def month_up(self):
    self.month_display += 1
    self.month_total += 1

  #this function holds all of the scenarios you will face in the game
  def school_scenarios(self):

    #makes completed_scenarios a global list
    global completed_scenarios
#Note: All the scenarios below are formatted the same so the comments will only be applied to the first two. The rest follow the same format
    #checks to see if the characters grade is 9 
    if self.grade == 9:
      #loop is created so that if a scenario that is already picked was picked again it would pick a new scenario.
      while True:
        #generates random number
        scenario = random.randint(1,6)
        #checks to see if the scenario has already been completed
        if scenario not in completed_scenarios:
          break
      #if the number generated = 1
      if scenario == 1:
        #checks to see if the scenario has been ran already
        if 1 not in completed_scenarios:
          #adds the scenario to the list completed_scenarios so it is not played again
          completed_scenarios.append(1)
          #loop created so that if the user inputs an invalid input it runs again until a valid input is made
          while True:
            #scenario is presented and the character is given options. The user then inputs an option
            x = input("A bully wants to take your lunch. \n What will you do? \n \n a= punch the bully \n b= give the bully your lunch \n c = run away \n")
            #if the input is 'a'
            if x == 'a':
              #a random number is generated
              fight = random.randint(1,2)
              #if the number generated is 1 teh character gets beat up
              if fight == 1:
                print("You got beat up")
                #character health goes down 10 points and loop is broken
                self.health -= 10
                print("OOF that one hurt. Your health just went down ten points")
                break
              #if the number generated is 2 the fight is won
              if fight == 2:
                print("You won")
                #character happiness goes up 10 points
                self.happiness += 10
                print("Congrats you surprisingly won! Your happiness went up 10 points")
                #the loop is broken
                break
            #if the user input is 'b'
            elif x == 'b':
              #character happiness goes down 10 points
              self.happiness -= 10
              print("That one was a blow to your self esteem. Your happiness went down 10 points")
              #loop is broken
              break
            elif x == 'c':
              #character smarts goes up 5 points
              self.smarts += 5
              print("Finally, you did something intelligent. Your smarts went up 5 points")
              #loop is broken
              break
            #if the user inputs any other input it prints 'Error' and the loop restarts
            else:
              print("Error")
      #if the number generated is 2       
      elif scenario == 2:
        #checks to see if this scenario was already completed
        if 2 not in completed_scenarios:
          #adds this scenario to completed_scenarios so it is not repeated
          completed_scenarios.append(2)
          #loop created so that if the user inputs an invalid input it runs again until a valid input is made
          while True:
            #scenario is presented and the character is given options. The user then inputs an option
            x = input("You are assigned a group project from your freshman technology teacher. What are you going to do? \n \n a= do all the work \n b= do none of the work \n c= split up the work evenly \n")
            #if the user input is a 
            if x == 'a':
              #character smarts goes up 10 points
              self.smarts += 10
              print("Congrats try hard. Your now THAT kid, but hey your smarts went up 10 points")
              #loop is broken
              break
            #if the user input is b
            elif x == 'b':
              #character popularity goes down 10 points
              self.popularity -= 10
              print("Ew. Now your THAT kid. No one likes you so you lost 10 popularity points")
              #loop is broken
              break
            #if the user input is c
            elif x == 'c':
              #charcter popularity goes up 5 points
              self.popularity += 5
              print("You're chill with your groupmates now. You gained 5 popularity points")
              #loop is broken
              break
            #if the user inputs any other input it prints 'Error' and the loop restarts
            else:
              print("Error")
#Note once again all the other scenarios follow the same format
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
            x = input("You are on the way to school and you can't find your id? What are you going to do? \n \n a= Take the L(OP) \n b= Try to sneak into school without it \n c= run back home \n")
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

  #allows the character to study and up their smarts
  def study(self):
    #checks to see if the character already studied in the current month.If they have it will not let them study again.
    if self.month_total in times_studied:
      print("We all know you aint studying more than once a month. Nice try")
    else:
      #adds the current month to the times_studied so they can only study once this month
      times_studied.append(self.month_total)
      print('You went to the library to study like a good boy. Your smarts went up 5 points.')
      #characters smarts go up 5 points
      self.smarts += 5

  #allows the character to workout and up their looks
  def workout(self):
    #checks to see if they worked out this month. If they have it will not let them.
    if self.month_total in times_workedout:
      print("You got your swole on so hard you broke the gym. Come back at a later time.")
    else:
      #adds the current month to times_workedout so they can oly work out once this month
      times_workedout.append(self.month_total)
      #loop will reask the question until a valid answer is inputted
      while True:
        #asks the user to input what they want to work on at the gym
        x = input("What are you working on? \n c = cardio \n f = flexibility \n w = weights \n p = pretend to do something \n")
        #generates a random number to see if the character injures themselves at a gym
        y = random.randint(1,10)
        #check to see if the randomly generated number is 1 and if it is it tells the character that they injured themselves at the gym.
        if y == 1:
          print("Nice job bozo. You injured yourself at the gym. Your health is now down 10 points.")
          #characters health goes down 10 points and then the loop is exited
          self.health -= 10
          break
        #checks to see if the user wanted to work on cardio
        elif x == 'c':
          print("The only other time I have you seen you ran that fast is into Wendy's when you heard they were having a deal. But hey your looks and health went up 5 points")
          #characters looks go up 5 points
          self.looks += 5
          #characters health goes up 5 points and exits loop 
          self.health += 5
          break
        #checks to see if the user wants to work on flexibility
        elif x == 'f':
          print("Maybe next time youll actually be able to touch your toes but at least you put in some effort. Your health went up 5 points")
          #characters health goes up 5 points and exits loop
          self.health += 5
          break
        #checks to see if the user wants to lift weights
        elif x== 'w':
          print("Damn the grind really is real. You actually broke a sweat. Not gonna lie im surprised. Your looks went up 10 points")
          #characters looks goes up 10 points and exits loop
          self.looks += 10
          break
        elif x== 'p':
          print("This is lowkey sad but hey what works for you works for me so your happiness went up 5 points.")
          #characters happiness goes up 5 points and exits loop
          self.happiness += 5
          break
        #if the user puts in any other input it prints "Error" and the loop restarts
        else:
          print("Error")
          
  #this function prevents any of the characters stats from going below 0 and above 100
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
      
  #this function advances the user a grade once they have completed 5 months there
  def grade_up(self):
    if self.month_display == 6:
      self.month_display = 1
      self.grade += 1
      
  #this function tells the users what moves they can make and returns their input.
  def moves(self):
    #loop repeats until the user inputs a valid move
    while True:
      #displays possible you can play 
      print("\n Moves: \n a = advance a month \n s = go study at the library \n w = go workout")
      #asks the user what move they want to play
      move = input("What is your next move \n")
      #if they want to advance a month  
      if move == 'a':
        print("\n \n \n \n \n \n \n \n \n \n \n")
        #the function month_up() is ran
        self.month_up()
        #the graphics are updated
        self.graphics()
        #the loop is exited
        break
      #if they want to study
      elif move == 's':
        #the function study() runs
        self.study()
        #the graphics are updated
        self.graphics()
      #if they want to workout
      elif move == 'w':
        #the function workout()  runs
        self.workout()
        #the graphics are updated
        self.graphics()
      #if the user inputs any other input it prints 'Error' and the loop restarts
      else:
        print("Error")
        
  #this function checks if you die or are dead
  def dead(self):
    #two random numbers are generated 
    death_number = random.randint(1,death_chance)
    kill_number = random.randint(1,death_chance)
    #if the two numbers that are generated are equal or the characters health is 0
    if self.health == 0 or death_number == kill_number:
      #the characters status is changed to dead
      self.status = "dead"

  #this function only runs if the characters status is dead
  def death(self):
    #a random number is generated and depending on the number that death situation will run
    #a random number is generated and depending on the number that death situation will run
    while self.status == "dead":
      x = random.randint(1,2)
      if x == 1:
        print("You died of an advil overdose \n Game Over")
        break
      if x == 2:
        print("You tripped and fell and drowned in the toilet. There was no poop in it though so you are all good. \n Game Over")
        break
    #a random number is generated and depending on the number that death situation will run
    x = random.randint(1,2)
    if x == 1:
      print("You died of an advil overdose \n Game Over")
    if x == 2:
      print("You tripped and fell and drowned in the toilet. There was no poop in it though so you are all good. \n Game Over")  
  #this function just tells the user that they graduated and won the game
  def graduate(self):
    while self.status == 'graduated':
      print("Congrats you have graduated. \n You won!")
      break
    
  #this function runs all of the graphics
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

    max_looks = 100
    current_looks = self.looks
    percentage = current_looks/max_looks

    if current_looks > 31:
        col = (46, 204, 113)
    elif current_looks > 13:
        col = (255, 111, 0)
    else:
        col = (178, 34, 34)
            
    pygame.draw.rect(screen, col, pygame.Rect(197, 707, 290*percentage, 25), 0)

    percentage2 = int(current_looks/max_looks * 100)
    myfont = pygame.font.SysFont('Chunkfive', 28)
    textsurface = myfont.render(str(percentage2), False, (255,255,255))
    screen.blit(textsurface,(195, 707, 290*percentage, 25))

    max_smarts = 100
    current_smarts = self.smarts
    percentage = current_smarts/max_smarts

    if current_smarts > 31:
        col = (46, 204, 113)
    elif current_smarts > 13:
        col = (255, 111, 0)
    else:
        col = (178, 34, 34)
        
    pygame.draw.rect(screen, col, pygame.Rect(197, 665, 290*percentage, 25), 0)

    percentage2 = int(current_smarts/max_smarts * 100)
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

    max_happiness = 100
    current_happiness = self.happiness
    percentage = current_happiness/max_happiness

    if current_happiness > 31:
        col = (46, 204, 113)
    elif current_happiness > 13:
        col = (255, 111, 0)
    else:
        col = (178, 34, 34)

    pygame.draw.rect(screen, col, pygame.Rect(197, 585, 290*percentage, 25), 0)

    percentage2 = int(current_happiness/max_happiness * 100)
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
    
    myfont = pygame.font.SysFont('Chunkfive', 25)
    textsurface = myfont.render(str(self.name), False, (40, 116, 166))
    screen.blit(textsurface,(60,55))
    
    myfont = pygame.font.SysFont('Chunkfive', 25)
    othergrade = myfont.render(str(self.grade), False, (40, 116, 166))
    ninthgrade = myfont.render("9th grade", False, (40, 116, 166))
    thgrade = myfont.render("th grade", False, (40, 116, 166))
    if self.grade == 9:
      screen.blit(ninthgrade,(68,70))
    else: 
      screen.blit(othergrade,(68,70))
      screen.blit(thgrade,(90,70))
      
    pygame.draw.rect(screen, (255, 255, 255), [410, 5, 80, 40])

    myfont = pygame.font.SysFont('Chunkfive', 18)
    textsurface = myfont.render('Become', False, (255, 193, 7))
    screen.blit(textsurface,(425,8))

    myfont = pygame.font.SysFont('Chunkfive', 18)
    textsurface = myfont.render('A', False, (255, 193, 7))
    screen.blit(textsurface,(422,20))

    myfont = pygame.font.SysFont('Chunkfive', 18)
    textsurface = myfont.render('Magnet', False, (40, 116, 166))
    screen.blit(textsurface,(435,20))

    myfont = pygame.font.SysFont('Chunkfive', 18)
    textsurface = myfont.render('Student', False, (255, 193, 7))
    screen.blit(textsurface,(428,30))


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

#this creates a character of the person class and asks the user to input their name
character = Person(input("What is your name (input first and last)?"),"alive",1,1,9,gender,50,happiness,health,smarts,looks)
#runs the graphics function
character.graphics()
#runs the introduce function
character.introduce()

#checks to see if the characters gender is alien
if character.gender == "alien":
  #prints alien text, changes character status and says the fbi found you
  print("⏁⊑⟒ ☌⟟⍀⌰ ⏃⏁ ⏁⊑⟒ ⏚⍜⍜⏁⊑ ⌇⍜⌰⎅ ⎎⟟⎎⏁⊬ ⏚⍜⋏⎅⌇. ⌰⍜⍜☍ ⟟⋏ ⏁⊑⟒ ☊⍜⍀⋏⟒⍀ ⏁⍜ ⎎⟟⋏⎅ ⏁⊑⟒ ⏁⏃⋏ ⌇⊑⟟⍀⏁.⏁⊑⟒ ☌⍀⟒⏃⏁ ⏃⋏⏁⟟⍾⎍⟟⏁⊬ ⍜⎎ ⋏⍜⏁⊑⟟⋏☌ ⟟⌇ ⏃⌿⌿⏃⍀⟒⋏⏁ ⎎⍀⍜⋔ ⟟⏁⌇ ⏚⟒⟟⋏☌ ⌇⍜ ⎐⟟⌇⟟⏚⌰⟒ ⟟⋏ ⏁⊑⟒ ⏃☊☊⍜⎍⋏⏁⌇ ⍙⟒ ⊑⏃⎐⟒ ⍜⎎ ⏁⊑⟒ ⏚⟒☌⟟⋏⋏⟟⋏☌ ⍜⎎ ⟒⎐⟒⍀⊬ ⋏⏃⏁⟟⍜⋏. ⏁⊑⟟⌇ ⟟⌇ ⎐⟒⍀⊬ ⌿⌰⏃⟟⋏⌰⊬ ⏁⍜ ⏚⟒ ⎅⟟⌇☊⍜⎐⟒⍀⟒⎅ ⟟⋏ ⏁⊑⟒ ⎎⟟⍀⌇⏁ ⌿⏃☌⟒⌇, ⏃⋏⎅ ⌇⍜⋔⟒⏁⟟⋔⟒⌇")
  character.status = 'alien'
  print('the fbi found you')

#loop only runs when the character's status is alive
while character.status == "alive":
  #runs the graohics function
  character.graphics()
  
  #checks to see if the character has played for 21 months. If so the character's status is changed to graduated and the loop is exited
  if character.month_total ==21:
          character.status = 'graduated'
          break
        
  #runs the grade_up() function
  character.grade_up()

  #runs the stats_constraints() function
  character.stats_constraints()

  #runs the dead() function
  character.dead()

  #runs the school_scenarios() function
  character.school_scenarios()
  
  #runs the graphics() function
  character.graphics()
  
  #checks to see if the characters status is ded(certain scenarios cause this) and if so it breaks the loop
  if character.status == "ded":
    break
  
  #runs the moves() function
  character.moves()

  #runs the graphics() function
  character.graphics()

  #runs the death() function
  character.death()

#runs the graduate function
character.graduate()
