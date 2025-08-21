userNo=int(input("enter any random number :-"))
if userNo%3==0 :
    if userNo%5==0 :
        print("FizzBuzz")
    else :
        print("Fizz")
elif userNo%5==0:
    print("Buzz")
else:
    print(userNo)
