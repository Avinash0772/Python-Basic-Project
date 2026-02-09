# INPUTS WE NEED FROM THE USER
# 1. Total rent
# 2. Total food ordered
# 3. Electricity units spend 
# 4. charge per unit
# 5. Persons linving in Flat


## OUTPUT 
# Total amount you've to pay is 

rent = int(input("Enter your flat rent = "))
food = int(input("Enter the amount of food oredered = "))
electricity_spend = int(input("Enter the total of electricity spend = "))
charge_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("Enter the number of persons living in flat = "))

if persons <= 0:
    print("Invalid number of persons")
    exit()

total_bill = electricity_spend * charge_per_unit

output = (food + rent + total_bill) // persons 

print("Each person will pay = ", output)