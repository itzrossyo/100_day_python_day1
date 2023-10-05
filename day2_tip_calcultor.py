print("welcome to the tip calculator!\n")
bill = float(input("please enter how much your bill was\n £"))
tip = int(input("how much would you like to tip 10, 12, 15, 20?\n"))
people = int(input("please enter how many people you wish to split the bill with\n"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = "{:.2f}".format(bill_per_person)

print(f"each person should pay £{final_amount}")
