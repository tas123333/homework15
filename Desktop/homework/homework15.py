number1 = int(input("write number one: "))
number2 = int(input("write number two: "))
i = number1
k = number1
if number1 < number2:
    while i < number2:
        print(i)
        i += 3

elif number1 == number2:
    print("both numbers are equal")
elif number1 > number2:
    while k > number2:
        print(k)
        k -=3
else:
    print("there is an error")

