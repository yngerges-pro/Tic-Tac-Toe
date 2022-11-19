import random
#exit function
def exitProgram():
  print("Nice Challenge!")
  exit()
#shows who won the game 
def when_done():
  
  if game[0][0] == "O" and game[0][1] == "O" and game[0][2] == "O":
    print("You win!")
    exitProgram()
  elif game[0][0] == "X" and game[0][1] == "X" and game[0][2] == "X":
    print("I win!")
    exitProgram()
  elif game[0][0] == "O" and game[1][1] == "O" and game[2][2] == "O":
    print("You win!")
    exitProgram()
  elif game[0][0] == "X" and game[1][1] == "X" and game[2][2] == "X":
    print("I win!")
    exitProgram()
  if game[0][0] == "O" and game[1][0] == "O" and game[2][0] == "O":
    print("You win!")
    exitProgram()
  elif game[0][0] == "X" and game[1][0] == "X" and game[1][0] == "X":
    print("I win!")
    exitProgram()
  if game[1][0] == "O" and game[1][1] == "O" and game[1][2] == "O":
    print("You win!")
    exitProgram()
  elif game[1][0] == "X" and game[1][1] == "X" and game[1][2] == "X":
    print("I win!")
    exitProgram()
  if game[2][0] == "O" and game[2][1] == "O" and game[2][2] == "O":
    print("You win!")
    exitProgram()
  elif game[2][0] == "X" and game[2][1] == "X" and game[2][2] == "X":
    print("I win!")
    exitProgram()
  if game[0][2] == "O" and game[1][1] == "O" and game[2][0] == "O":
    print("You win!")
    exitProgram()
  elif game[0][2] == "X" and game[1][1] == "X" and game[2][0] == "X":
    print("I win!")
    exitProgram()
  if game[0][2] == "O" and game[1][2] == "O" and game[2][2] == "O":
    print("You win!")
    exitProgram()
  elif game[0][2] == "X" and game[1][2] == "X" and game[2][2] == "X":
    print("I win!")
    exitProgram()
  if game[0][1] == "O" and game[1][1] == "O" and game[2][1] == "O":
    print("You win!")
    exitProgram()
  elif game[0][1] == "X" and game[1][1] == "X" and game[2][1] == "X":
    print("I win!")
    exitProgram()
 
  
#displays the table
def Table():
  for x in range(len(game)):
    print(game[x], sep=" ")
    
#declares game, prints game, and collects user input
game = [[1,2,3],[4,5,6],[7,8,9]]
print("tic tac toe: \n")
Table()
print("\nto quit: type 0")
choice = int(input("\nYou are 'O': choose a number between 1-9: "))
arr = []
arr.append(choice)



  
#allows the user to pick first
def Main_function(choice):
  count = 0
  print(" ")
  if choice <= 9 and choice >= 0:
    if choice == 0:
      exitProgram()
    elif choice <= 3 and choice > 0:
      game[0][int(choice-1)] = "O"
      Table()
      count = count + 1
      when_done()
    elif int(choice) > 3 and int(choice) <= 6:
      game[1][int(choice - 4)] = "O"
      Table()
      count = count + 1
      when_done()
    elif int(choice) > 6 and int(choice) <= 9:
      game[2][int(choice - 7)] = "O"
      Table()
      count = count + 1
      when_done()
    else:
      return "wrong choice"
     
    # for x in range(len(game)):
    #   print(game[x], sep=" ")
    # return "\nMy Turn "
  else:
    return "Wrong choice"
#first function called
Main_function(choice)


#does not choose the same number as the user
def computer_choice(ran,choice):
  print("\nMy Turn ")
  #Space
  print(" ")
  if ran <= 9 and ran > 0:
    if choice == 0:
      exitProgram()
    elif ran <= 3:
      game[0][int(ran)-1] = "X"
      Table()
      when_done()
    elif int(ran) > 3 and int(ran) <= 6:
      game[1][int(ran) - 4] = "X"
      Table()
      when_done()
    elif int(ran) > 6 and int(ran) <= 9:
      game[2][int(ran) - 7] = "X"
      Table()
      when_done()
    else:
      return "Wrong choice!"
    # for i in range(len(game)):
    #   print(game[i], sep= " ")
    # return "\n"
  
  else:
      return "Wrong choice!"

#function checks for computer mistakes
#such as choosing the same number as
#the user or using a number that
#is already used
def no_mistakes(choice):
  compchoice = []
  #chooses a number
  ran = random.randint(1,9)
  #randomly selects a number that is not the same 
  #as the user's input or not already taken
  #avoids choosing the same number
  ## print("inputs:", arr)
  while ((ran in arr) or (ran in compchoice) or (ran == choice)):
    ran = random.randint(1,9);
  arr.append(ran)
  ## print("all inputs:", arr)
  #after checking for mistakes
  #calls for the function, computer_choice
  return computer_choice(ran,choice)


#second function called
no_mistakes(choice)


print(" ")
choice = int(input("\nYour Turn: "))
arr.append(choice)

def replyToComputer():
  #third function that is called again
  Main_function(choice)


  
number = [1,2,3,4,5,6,7,8,9]
if choice in number:
    replyToComputer()
else:
  print("wrong choice")

no_mistakes(choice)

#space
print("")
while choice != 0:
  #space
  print("")
  choice = int(input("Your turn again: "))
  Main_function(choice)
  arr.append(choice)
  no_mistakes(choice)