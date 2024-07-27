logo="""
  _______             _______ _     _     _                                                                      
 |__   __|           |__   __| |   (_)   | |                                                                     
    | |_ __ _   _       | |  | |__  _ ___| |                                                                     
    | | '__| | | |      | |  | '_ \| / __| |                                                                     
    | | |  | |_| |      | |  | | | | \__ |_|                                                                     
    |_|_|   \__, |      |_|  |_| |_|_|___(_)                                                                     
             __/ |                                                                         
            |___/                                                                       
  _   _                 _                  _____                                     _____
 | \ | |               | |                / ____|                  (_)              / ____|                      
 |  \| |_   _ _ __ ___ | |__   ___ _ __  | |  __ _   _  ___ ___ ___ _ _ __   __ _  | |  __  __ _ _ __ ___   ___  
 | . ` | | | | '_ ` _ \| '_ \ / _ | '__| | | |_ | | | |/ _ / __/ __| | '_ \ / _` | | | |_ |/ _` | '_ ` _ \ / _ \ 
 | |\  | |_| | | | | | | |_) |  __| |    | |__| | |_| |  __\__ \__ | | | | | (_| | | |__| | (_| | | | | | |  __/ 
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \_____|\__,_|\___|___|___|_|_| |_|\__, |  \_____|\__,_|_| |_| |_|\___| 
                                                                             __/ |                               
                                                                            |___/                                
                                                                            """


print(logo)

print("welcome to the number guessing game!")
print("I'm thinking a number between 1 to 100")
import random
computer_choice=random.randint(1,100)


#print(computer_choice)



choices=(input("choose the difficulty level .Type \"Hard\" or \"Easy\" :  ")).lower()
attempts=10
if choices=="hard":
    attempts=attempts-5
    print(f"ypu have {attempts} attempts.")
elif choices=="easy":
    attempts=10
    print(f"you have {attempts} attempts.")
else:
    print("invalid ,")
    attempts=10

while attempts>0:
        print(f"You have {attempts} left !")
        attempts-=1
        user_guesses=int(input("Guess the number: "))
        if user_guesses<computer_choice:
                      print("Too Low!")
                     
        elif user_guesses>computer_choice:
                      print("Too High")                             
        else:
                      print(f"You've gussed the correct number which is {computer_choice}")
                      break
else:
              print(f"sorry,you've run out of attempts. The correct number was {computer_choice}")
       