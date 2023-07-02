import random
print("General instructions: \n Type R for rock \n Type P for paper \n Type S for scissors \n Best of three wins")
user_score=0
computer_score=0
ready = int(input("Ready to play ? --> (type 1 to play)"))
if ready == 1 :
    print("Lets get started...")
    r=0
    for x in range(0,3):
     options = ["r", "p", "s"]
     r=r+1
     print("###Round###",r)
     user_options = input("Choose among (R,P,S) -->").lower()

     if user_options not in options:
         print("Please enter a valid value")
     else:
      computer_options = ["r" , "s" ,"p"]
      computer_choice = random.choice(computer_options)
      print("Computer choosed", computer_choice)
      if user_options == "r" and computer_choice == "s":
          print("You won")
          user_score+=1
          print("Your score = ",user_score)
          print("Computer score = ",computer_score)
      elif user_options == "p" and computer_choice == "r":
          print("You won")
          user_score+=1
          print("Your score = ",user_score)
          print("Computer score = ",computer_score)
      elif user_options == "s" and computer_choice=="p":
          print("You won")
          user_score+=1
          print("Your score = ",user_score)
          print("Computer score = ",computer_score)
      elif user_options == computer_choice:
          print("Its a tie")
          print("Your score = ",user_score)
          print("Computer score = ",computer_score)
      else:
          computer_score+=1
          print("Computer won")
          print("Computer score = ",computer_score)
          print("Your score = ",user_score)
    s="Final Result"
    print(s.center(20,"#"))
    if user_score>computer_score: 
     print("You won the game !!")
    elif user_score==computer_score:
     print("Its a tie")
    else: 
     print("You lost the game")
     
else :
    print("Bye")
    quit()
