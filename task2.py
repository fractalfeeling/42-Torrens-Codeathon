import csv
import sys
import os
from operator import itemgetter

company_list = []
p1_list = [0]
p2_list = [0]
p3_list = [0]
r_list = [0]
class Startup:
    def __init__(self, company):
        self.name = company[0]
        self.factor1 = float(company[1])
        self.factor2 = float(company[2])
        self.factor3 = float(company[3])
        self.factor4 = float(company[4])
        self.rating = self.rating()
        self.category = self.category()

    def rating(self):
        r = (0.30 * self.factor1 + 0.30 * self.factor2
                + 0.35 * self.factor3 + 0.05 * self.factor4)
        return round(r, 2)

    def category(self):
        if self.rating >= 4.0 and self.rating <= 5.0:
            p1_list[0] += 1
            p1_list.append(self.name)
            return "P1"
        elif self.rating >= 2.5 and self.rating < 4.0:
            p2_list[0] += 1
            p2_list.append(self.name)
            return "P2"
        elif self.rating >= 1.0 and self.rating < 2.5:
            p3_list[0] += 1
            p3_list.append(self.name)
            return "P3"
        elif self.rating >= 0 and self.rating < 1.0:
            r_list[0] += 1
            r_list.append(self.name)
            return "R"

# a bunch of error testing

try:
    test = open("startups.csv", "x")
    test.close()
    os.remove("startups.csv")
except FileExistsError:
    answer = ""
    print("Warning: startups.csv already exists, continuing will overwrite previous data!")
    while True:
        answer = input("Are you sure you want to continue? Enter Y or N:\n")
        if answer == "N" or answer == "n":
            print("Selected 'N', please rename the existing startups.csv and restart program.")
            sys.exit()
        elif answer == "Y" or answer == "y":
            while True: # double checking in case of accidental input
                answer = input("Are you 100% sure you want to overwrite ALL the existing data in 'startups.csv' ?\n")
                if answer == "Y" or answer == "y":
                    break
                elif answer == "N" or answer == "n":
                    print("Selected 'N', please rename the existing startups.csv and restart program.")
                    sys.exit()
                else:
                    print("Invalid input, please try again\n")
            try:
                test = open("startups.csv", "a")
                test.close()
            except PermissionError: # This happened while testing and realised I was getting this error because I had the csv file open in Excel
                print("Error: Unable to overwrite 'startups.csv' !\nCheck file permissions or whether 'startups.csv' "
                      "is open in another program and then restart program.")
                sys.exit()
            print("Selected 'Y', program will overwrite existing the existing startups.csv file\n")
            print("DO NOT OPEN 'startups.csv' WHILE THE PROGRAM IS RUNNING\n")
            break
        else:
            print("Invalid input, please try again\n")

indexerr = 0

def float_check(founder, industry, traction, gut):
    if float(founder) < 0 or float(founder) > 5.0:
        return False
    if float(industry) < 0 or float(industry) > 5.0:
        return False
    if float(traction) < 0 or float(traction) > 5.0:
        return False
    if float(gut) < 0 or float(gut) > 5.0:
        return False
    score = round(((float(founder) * 0.3)  + (float(industry) * 0.3) + (float(traction) * 0.35) + (float(gut) * 0.05)), 2)
    if score >= 0 and score <= 5.0:
        return True
    else:
        return False

while True:
    try:
        company = input("When finished with input, enter 'N'\nEnter a Start-up's factor ratings (separated by comma):\n")
        if company == "N" or company == "n" and len(company) == 1:
            break
        if company.count(",") != 4: # This is for an error if you only put in text and no commas, you get a ZeroDivisionError later
            company = ""
            print("Input error!\nExample input: 'My Company,1.5,2.3,4.7,0.2\n")
        else:
            company = company.split(",")
            if len(company) == 5:
                try:
                    if float_check(company[1], company[2], company[3], company[4]) == False:
                        print("Input Error! Factor ratings must be on a scale of 5\nExample input: 'My Company,1.5,2.3,4.7,0.2'\n")
                    else:
                        company_list.append(Startup(company))
                except ValueError:
                    print("Input Error! Please enter 4 numbers for the Start-Ups factor ratings!")
                    print(company_list)
            else:
                print("Input Error! Please try again\nExample input: 'My Company,1.5,2.3,4.7,0.2'\n")

    except IndexError:
        indexerr += 1
        print("Input Error!\nPlease input the Start-up's name followed a comma "
              "and their 4 ratings separated by commas") if indexerr < 3 else print("Input Error!\nExample input: 'My Company,1.5,2.3,4.7,0.2'\n")


num_startup = len(company_list)

def object_to_array(company_list):
    array_list = []
    for company in company_list:
        array_list.append([company.name, company.factor1, company.factor2,
        company.factor3, company.factor4, company.rating, company.category])
    return array_list

company_arrlist = object_to_array(company_list)
company_arrlist.sort(key = itemgetter(5), reverse = True)

def average_factor(n):
    avg = 0
    for i in range(0, num_startup):
        avg += company_arrlist[i][n]
    return avg / num_startup

try:
    progression_rate = (p1_list[0] + p2_list[0] + p3_list[0]) / num_startup * 100
    print("Number of Start-ups: %d" % num_startup)
    print("Start-up progression rate: %.f%%" % progression_rate)
    print("Average rating for factor 1: %.2f" % average_factor(1))
    print("Average rating for factor 2: %.2f" % average_factor(2))
    print("Average rating for factor 3: %.2f" % average_factor(3))
    print("Average rating for factor 4: %.2f" % average_factor(4))
    print("Number of P1s: %s" % ", ".join(str(i) for i in p1_list))
    print("Number of P2s: %s" % ", ".join(str(i) for i in p2_list))
    print("Number of P3s: %s" % ", ".join(str(i) for i in p3_list))
    print("Number of Rs: %s" % ", ".join(str(i) for i in r_list))
except ZeroDivisionError:
    print("No valid inputs entered, restart program to try again")

try:
    with open("startups.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(["Company Name", "Founder", "Industry", "Traction", "Gut", "Rating", "Classification"])
        writer.writerows(company_arrlist)
except PermissionError:
    print("Unable to overwrite to 'startups.csv', did you open the file while the program was running?\nClose 'startups.csv' and restart program to try again.")
