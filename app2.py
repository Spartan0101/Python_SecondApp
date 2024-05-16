#Tip calculator

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
bill_with_tip = tip / 100 * bill + bill
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")




#number = input()
#a = int(number[0])
#b = int(number[1])
#print(a + b)

#Body mass index calculator

#height = input()
#weight = input()
#weight_as_int = int(weight)
#height_as_float = float(height)
#bmi = weight_as_int / (height_as_float ** 2)

#bmi_as_int = int(bmi)
#print(bmi_as_int)

#f-String

#score = 0
#height = 1.8
#isWinning = True
#print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")

#age = input("Age: ")
#life_left = (90 - int(age)) * 52
#print(f"You have {life_left} weeks left.")
