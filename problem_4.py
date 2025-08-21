secret_number=10
print("Wellcome to game whose name is ....is ...")
print(".........guess the secret  number.........")
while True:
    user_guess=int(input("Enter the guess  :- "))
    if(user_guess==secret_number):
        print("<<<congratulation>>> your guess is correct")
        break
    if user_guess-secret_number<0:
        if secret_number-user_guess<=10:
            distance="low"
        else:
            distance="too low"
    elif user_guess-secret_number>0:
        if user_guess-secret_number<=10:
            distance="high"
        else:
            distance="too high"
        
    print(f"<<<sorry>>> your guess is {distance} from the secret number")
    print("try again")
