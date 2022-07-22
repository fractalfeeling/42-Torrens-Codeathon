def ask():
    decision = input("Would you like to try again? (enter Y to yes, or N to no)")
    if (decision == 'Y' or decision == 'y'):
        program()
    elif (decision =='N' or decision == 'n'):
        quit()
    else:
        print('Input invalid')
        ask()
        
def program():
    try:
        ratings = [item for item in input("Enter a Start-up's factor ratings (separated by comma):\n").split(',')]
        val1 = float(ratings[1])
        val2 = float(ratings[2])
        val3 = float(ratings[3])
        val4 = float(ratings[4])
        score = (val1 * 0.3) + (val2 * 0.3) + (val3 * 0.35) + (val4 * 0.05)
        score = round(score, 2)
        if (val1<0 or val1>5):
            print('Rating 1 must be on a scale of 0 to 5')
            ask()
        elif (val2<0 or val2>5):
            print('Rating 2 must be on a scale of 0 to 5')
            ask()
        elif (val3<0 or val3>5):
            print('Rating 3 must be on a scale of 0 to 5')
            ask()
        elif (val4<0 or val4>5):
            print('Rating 4 must be on a scale of 0 to 5')
            ask()
        else:
            if score >= 4.0:
                print("P1")
            elif score >= 2.5:
                print("P2")
            elif score >= 1.0:
                print("P3")    
            else:
                print("R")
    except ValueError:
        print("Please input numbers for ratings")
        ask()
    except IndexError:
        print("Please input 4 ratings")
        ask()

program()
