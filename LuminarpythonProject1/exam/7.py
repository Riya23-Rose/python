n=int(input("enter your number"))
if n%15==0:
    print("fizzbuzz")
elif n%5==0:
    print("buzz")
elif n%3==0:
    print("fizz")
else:
    print("invalid")