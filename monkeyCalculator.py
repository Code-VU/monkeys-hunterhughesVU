def calculateTime():
    
    # This first line is provided for you
    monkey_one = input("Is the first monkey smiling?:  ")
    monkey_two = input("Is the second monkey smiling?: ")

    yes = 0

    if(monkey_one == 'y'):
        yes += 1
    if(monkey_two == 'y'):
        yes += 1

    if(yes == 1):
        print("Yay! We're going to have a good day!")
    
    else:
        print("Uh Oh! We're in trouble!")

    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateTime() and run > python monkeyCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
#calculateTime()