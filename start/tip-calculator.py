print("Welcome to the tip calculator.")
receive_bill = float(input("What was the total bill? $"))
receive_percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
receive_people = float(input("How many people to split the bill? "))

count_percentage = receive_percentage / 100
count_bill = receive_bill * count_percentage
total_bill = receive_bill + count_bill
bill_person = total_bill / receive_people
final_bill = (round(bill_person, 2))
print(f"Each person should pay: ${final_bill}")