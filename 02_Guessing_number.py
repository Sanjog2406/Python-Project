import random 
n = random.randint(1,100)
a = 1
guess = 1

while(a!=n):
    a = int(input("Guess the number : "))
    if(a<n):
        print("Enter the higher number")
        guess+= 1

    elif(a>n):
        print("Enter the smaller number")

        guess+= 1
 
print(f"You guess {n} in {guess} attempts")
