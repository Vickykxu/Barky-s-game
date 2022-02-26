import random
######################################
# My lists
######################################
actions = ["Surrender","Open bag","Attack"]
allies = ["Mr. Quackers", "Mr. Chubs", "Squishy"]
allies_health = [30, 25, 50]
enemies = ["Billy the Pig", "Sally the Sheep", "Hoe the Horse"]
barky_attack = ["Double Kick", "1-2!","Surprise Tickles", "Power Punch","Fast Dash","Charge Up"]
enemy_attack = ["Blame", "Slap", "Tug", "Sneeze", "Splash"]
items = ["A bag of carrots (+25 health)","Blankie (Summon an ally)", "Wagon (Dodge next enemy attack)", "Barky's triangle (Enemy becomes confused)"]
bag = []

######################################
# Non-lists
######################################
barky_health = 100
enemy_health = 100
current_enemy = (random.choice(enemies))
current_player_barky = True
ally_in_play = False
ally_choice = (random.choice(allies))
ally_chosen_health = 0
skip_turn = False

######################################
# Enemy's attack moves (Function)
######################################
# Has a 75% chance of hitting. If ally is alive, have the ally take the damage (10 health). If not, Barky loses 10 health. If the move misses, the enemy loses 5 health.
def blame():
  num = random.randint(1,4)
  if num == 1 or num == 2 or num == 3:
    global current_enemy
    print(current_enemy, "used blame on Barky. Now everyone is mad at him.")
    if ally_meat_shield(10) == False:
      global barky_health
      barky_health -= 10
      print("Barky's health: " ,str(barky_health + 10), "-->" ,str(barky_health))
    global ally_choice 
    global ally_chosen_health
    print(ally_choice, "'s health:", str(ally_chosen_health))
  else:
    print(current_enemy, "tried to use blame, but Barky is a good boy and got away with it. Now everyone is mad at ", current_enemy)
    global enemy_health
    enemy_health -= 5
    print(current_enemy, "'s health':" ,str(enemy_health + 5), "-->" ,str(enemy_health))
    
# Guaranteed to hit. If ally is alive, have the ally take the damage (7 health). If not, Barky loses 7 health.    
def slap():
  global current_enemy
  print(current_enemy, "used slap on Barky. Ouch that's got to hurt...")
  if ally_meat_shield(7) == False:
    global barky_health
    barky_health -= 7
    print("Barky's health: " ,str(barky_health + 7), "-->" ,str(barky_health))
  global ally_choice 
  global ally_chosen_health
  print(ally_choice, "'s health:", str(ally_chosen_health))

# Has a 33% chance of hitting. If ally is alive, have the ally take the damage (15 health). If not, Barky loses 15 health.
def tug():
  global current_enemy
  num = random.randint(1,3)
  if num == 1:
    print(current_enemy, "started tugging on Barky's ears. Oh no, not his sad ears")
    if ally_meat_shield(15) == False:
      global barky_health
      barky_health -= 15
      print("Barky's health: " ,str(barky_health + 15), "-->" ,str(barky_health))
    global ally_choice 
    global ally_chosen_health
    print(ally_choice, "'s health:", str(ally_chosen_health))
  else:
    print(current_enemy, "missed the tug on Barky's ears")

# Guaranteed to hit. If ally is alive, have the ally take the damage (12 health). If not, Barky loses 12 health. Enemy also loses 8 health as a result.
def sneeze():
  global current_enemy
  print(current_enemy, "sneezed on Barky. Barky is now enraged and sneezes on ", current_enemy)
  global enemy_health
  enemy_health -= 8
  print(current_enemy, "'s health':" ,str(enemy_health + 8), "-->" ,str(enemy_health))
  if ally_meat_shield(12) == False:
    global barky_health
    barky_health -= 12
    print("Barky's health: " ,str(barky_health + 12), "-->" ,str(barky_health))
  global ally_choice 
  global ally_chosen_health
  print(ally_choice, "'s health:", str(ally_chosen_health))

# Has a 50% chance of landing. If the ally is alive, have the ally take the damage (7 health). If not, Barky loses 7 health.
def splash():
  global current_enemy
  global barky_health
  num = random.randint(1,2)
  if num == 1:
    print(current_enemy, "splashed Barky with water and got his fur all wet")
    if ally_meat_shield(10) == False:
      global barky_health
      barky_health -= 10
      print("Barky's health: " ,str(barky_health + 10), "-->" ,str(barky_health))
    global ally_choice 
    global ally_chosen_health
    print(ally_choice, "'s health:", str(ally_chosen_health))
  else: 
    print(current_enemy, "missed the splash on Barky")
  

######################################
# Barky's attack moves (Functions)
######################################
# Has a 20% chance of hitting, and enemy dies instantly. If it misses, Barky takes 15 damage
def double_kick():
  num = random.randint(1,10) 
  if num == 1 or num == 2:
    print("Barky tried to use Double Kick... It was effective and he knocks out " + current_enemy)
    global enemy_health
    enemy_health = 0
  else:
    print("Barky tried to use Double Kick... Barky fell on his butt and the kick was not successful")
    global barky_health
    barky_health -= 15
    print("Barky's health:" ,str(barky_health + 15), "-->" ,str(barky_health))

# Guaranteed to hit and the enemy loses 7 health
def one_two():
  print("Barky used 1-2! It wasn't very effective...")
  global enemy_health
  enemy_health -= 7
  print(current_enemy, "'s health':" ,str(enemy_health + 7), "-->" ,str(enemy_health))

# Has a 50% chance of hitting, and enemy loses 12 health. If it misses, there is are no repercussions
def surprise_tickles():
  num = random.randint(1,10)
  chance2 = num%2
  if chance2 == 0:
    print("Barky tried to use surprise tickles, and it was effective!")
    global enemy_health
    enemy_health -= 12
    print(current_enemy, "'s health':" ,str(enemy_health + 12), "-->" ,str(enemy_health))
  else:
    print("Barky tried to use Surprise Tickles, and " + current_enemy + " dodged it")

# Has a 25% chance of hitting, and enemy loses 20 health. If it misses, there are no repercussions
def power_punch():
  num = random.randint(1,4)
  if num == 1:
    print("Barky tried to use Power Punch, and it was super effective")
    global enemy_health
    enemy_health -= 20
    print(current_enemy, "'s health':" ,str(enemy_health + 20), "-->" ,str(enemy_health))
  else:
    print("Barky tried to use Power Punch and it missed")

# Has a 75% chance of hitting, and enemy loses 12 health. If it misses, deals 7 damage to Barky
def fast_dash():
  num = random.randint(1,4)
  if num == 1 or num == 2 or num == 3:
    print("Barky tried to use Fast Dash, and it was super effective")
    global enemy_health
    enemy_health -= 12
    print(current_enemy, "'s health':" ,str(enemy_health + 12), "-->" ,str(enemy_health))
  else:
    print("Barky slipped on the puddle of water he left behind ouch!")
    global barky_health
    barky_health -= 7
    print("Barky's health:" ,str(barky_health + 7), "-->" ,str(barky_health))

# Barky gains 5 health on his turn
def charge_up():
  global barky_health
  barky_health += 5
  print("Barky's health:" ,str(barky_health - 5), "-->" ,str(barky_health))

######################################
# Item and Bag Usage (Functions)
######################################
# Opens the bag and lists the items inside. Also asks users if they would like to use an item
def open_bag():
  print("===============================================================")
  bag_is_open = True
  while bag_is_open == True:
    print("In your bag you have...")
    for x in range(len(bag)):
      print([x], items[int(bag[x])])
    print("Do you want to use an item?")
    global item_choice
    using_item = input("" + username + ": ").lower()
    if using_item == "yes" or using_item == "y":
      print("Which one?")
      item_choice = (int(input("" + username + ": ")))
      print(item_choice)
      if item_choice <= len(bag):
        item_use(item_choice)
        del bag[item_choice]
        bag_is_open = False
    elif using_item == "no" or using_item == "n":
     bag_is_open = False
  print("================================================================")

# Using an item (goes through all 4 cases) 
# Passes item choice as argument, where item choice is a number corresponding to the item you want to use
def item_use(item_choice):
  item_choice_idx = bag[item_choice]
  if (item_choice_idx == 0):
    print("You gave Barky a bag of carrots, yummy!")
    global barky_health
    barky_health += 25
    print(str(barky_health - 25), "-->" ,str(barky_health))
  elif (item_choice_idx == 1):
    global ally_choice
    global ally_chosen_health
    print("You summoned " + ally_choice + "!")
    ally_helper(item_choice)
    ally_chosen_idx = allies.index(ally_choice)
    ally_chosen_health = allies_health[ally_chosen_idx]
  elif (item_choice_idx == 2):
    print("Barky hops on Wagon and speeds away! He dodges the next attack. ")
    global skip_turn
    skip_turn = True
  else:
    print("Barky plays his triangle so loud it makes the enemy confused!")
    global enemy_health 
    enemy_health -= 20
    print(current_enemy, "'s health':" ,str(enemy_health + 20), "-->" ,str(enemy_health))

######################################
# Health System (Functions)
######################################

# Shows the health board throughout the game. If an ally is summoned, show health bar for it too
def health_system():
  print("HEALTH BARS")
  print("Barky:", str(barky_health))
  print((current_enemy)+":", str(enemy_health))    
  if ally_in_play == True:
    global ally_choice
    global ally_chosen_health
    print(ally_choice, ":", ally_chosen_health)
  print("================================================================")

# If user chooses to use Blankie, set ally_in_play = True
# Passes item choice as argument, where item choice is a number corresponding to the item you want to use 
def ally_helper(item_choice):
  item_choice_idx = bag[item_choice]
  if item_choice_idx == 1:
    global ally_in_play
    ally_in_play = True
  print("================================================================")

# If ally is still alive, have the damage reflected to ally instead of Barky
# Passes damage taken as argument
# Returns true if ally is still alive and false if not
def ally_meat_shield(dmg_taken):
  global ally_chosen_health
  if ally_chosen_health > 0:
    ally_chosen_health -= dmg_taken
    print(ally_choice ,str(ally_chosen_health + dmg_taken ), "-->" ,str(ally_chosen_health))
    return True
  else: 
    return False

######################################
# Logistics of the Game (Functions)
######################################

# Display list of actions for users to choose (menu)
def display_actions():
  print("What would you like to do?")
  for x in range(3):
    print([x], actions[x])  

# Display possible attacks for user to choose and run corresponding functions
def attack():
  print("================================================================")
  for x in range(6):
    print([x], barky_attack[x])
  print("Barky is ready. What move should he use?")
  attack_choice = input("" + username + ": ") 
  if attack_choice == "0":
    double_kick()
  elif attack_choice == "1":
    one_two()
  elif attack_choice == "2":
    surprise_tickles()
  elif attack_choice == "3":
    power_punch()
  elif attack_choice == "4":
    fast_dash()
  elif attack_choice == "5":
    charge_up()
  print("================================================================")

# Alternate turns between user and enemy
def switch_turn():
  global current_player_barky
  if current_player_barky == True:
    current_player_barky = False
  else:
    current_player_barky = True

######################################
# Driver
######################################


#Introduction to the game, and choosing a loadout (2 items)
print("Welcome to Barky's game!\nHelp guide Barky in defeating his enemies" )
print("What is your name?")
username = input("You: ")
print("It's nice to meet you " + username + "! Are you ready to play? (Y/N)")
user_ready = input("" + username + ": ").lower().strip("! ")
if user_ready == "y" or user_ready == "yes":
  print("=================================================================")
  print("Awesome! Before playing please choose your loadout.\nYou can hold a maximum of 2 items in your bag")
  for x in range(4):
    print([x], items[x])
    choice1 = False
    choice2 = False
  while choice1 == False:
    first_choice = input("What is your first item? (number) ")
    first_choice_int = (int(first_choice))
    if (int(first_choice) < len(items)):
      bag.append(first_choice_int)
      choice1 = True
  while choice2 == False:
      second_choice = input("What is your second item? (number) ")
      second_choice_int = (int(second_choice))
      if (int(first_choice) < len(items)):
        bag.append(second_choice_int)
        choice2 = True


# Running of the game         
  print("======================LET THE GAME BEGIN!======================")
  print("Your opponent is...", current_enemy)
  while ((barky_health > 1) and (enemy_health > 1)):
    if skip_turn == True:
      current_player_barky = True
      num = random.randint(1,2)
      if num == 1:
        skip_turn = False
        current_player_barky = False
        print(current_enemy, "is no longer confused and is ready to fight!")
      else: 
        print (current_enemy, "is confused, they will miss their go.")
    if current_player_barky == True:
      print("=========================Barky's turn!=========================")
      health_system()
      display_actions()
      user_action = input(username + ": ")
      if user_action == "1":
        open_bag()
      elif user_action == "0":
        print("Aww man. Barky sadly puts his paws up as he steps down from the fight.\nHis enemy laughs at him as he is forced to leave the battleground :(")
        print("Thank you for playing")
        barky_health = 0
      elif user_action == "2":  
        attack()
    else:
      print("==================",current_enemy,"'s turn!==================")
      enemy_attack_choice = random.choice(enemy_attack)
      if enemy_attack_choice == "Blame":
        blame()
      elif enemy_attack_choice == "Slap":
        slap()
      elif enemy_attack_choice == "Tug":
        tug()
      elif enemy_attack_choice == "Sneeze":
        sneeze()
      else:
        splash()
    switch_turn()
print("===========================The game ended==========================")