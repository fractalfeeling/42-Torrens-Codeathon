import csv
from operator import itemgetter

P1 = []
P2 = []
P3 = []
R = []
with open("startups.csv") as csvfile:
    reader = csv.reader(csvfile)
    if reader:
        next(reader)
    for line in reader:
        if line[6] == "P1":
            P1.append(tuple(line))
        elif line[6] == "P2":
            P2.append(tuple(line))
        elif line[6] == "P3":
            P3.append(tuple(line))
        elif line[6] == "R":
            R.append(tuple(line))

P1.sort(key = itemgetter(5), reverse = True)
P2.sort(key = itemgetter(5), reverse = True)
P3.sort(key = itemgetter(5), reverse = True)
R.sort(key = itemgetter(5), reverse = True)
startup_list = P1 + P2 + P3 + R
num_startup = len(startup_list)

def present_classification(option):
    d_opt = {'1': P1, '2': P2, '3': P3, '4': R}
    d_cls = {'1': 'P1', '2': 'P2', '3': 'P3', '4': 'R'}
    if len(d_opt[option]):
        for company in d_opt[option]:
            print(company[0] + ", Score: " + company[5])
    else:
        print("No startup satisfied requirement for %s ratings" % d_cls[option])

def present_invest(n):
    i = 0
    if n > num_startup:
        print("The number of businesses you want to invest in is more than currently available.")
        print("Showing %d available startups." % num_startup)
    while i < n and i < num_startup:
        print(startup_list[i][0] + ", " + startup_list[i][6] + ", Score: " + startup_list[i][5])
        i += 1

def user_input():
    try:
        option = input("Which option do you want to see: ")
        if option == '6':
            print("Program exit.")
            return 6
        elif option == '5':
            n = input("How many businesses do you want to invest in: ")
            present_invest(int(n))
        else:
            present_classification(option)
    except KeyError:
        print("Invalid option, please re-select.")
    except ValueError:
        print("Invalid input, please enter a number.")

return_val = 0

while True:
    print("-Start-Up Classification Menu-")
    print("1. Present all P1")
    print("2. Present all P2")
    print("3. Present all P3")
    print("4. Present all R")
    print("5. How many businesses do you want to invest in")
    print("6. Terminate\n")
    return_val = user_input()
    if return_val == 6:
        break
    print("")