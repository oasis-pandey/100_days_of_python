print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

total = (bill* (tip/100) + bill)
per_person = round((total/people),2)

print(f"The amount of bill per person is {per_person}")