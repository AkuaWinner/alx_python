#import random

#number = random.randint(-10, 10)

#print("The number:", number)

#if number > 0:
#    print("is positive")
#elif number == 0:
#    print("is zero")
#else:
    #print("is negative")


numbers = [-4, 0, -3, -10, 10, -5, 6, 7, 5]

for number in numbers:
    print(number, end=" ")
    if number > 0:
        print("is positive")
    elif number == 0:
        print("is zero")
    else:
        print("is negative")