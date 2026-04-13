print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill?\n $"))
tip_percent = int(input("How much tip would you like to give? 10,12 or 15?\n"))
final_bill = total_bill * (tip_percent/100) + total_bill
no_of_people = int(input("How many people to split the bill?\n"))
split_bill =  round((final_bill / no_of_people),2)
print(f"Each person should pay: ${split_bill}")
