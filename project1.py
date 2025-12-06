num_of_people_living = int(input('Enter Number of people living in the Flat : '))
Rent_for_month = int(input('Enter Monthly Rent of Flat : '))
Electricity_Consumed = int(input('Enter How many Units of Electricity Consumed : '))
Utilities_bills = int(input('Enter Amount for Utilities : '))
Groceries_bills = int(input('Enter Amount for Groceries : '))

if Electricity_Consumed >= 1 and Electricity_Consumed < 100:
    charge_for_unit = 5
elif Electricity_Consumed >= 100 and Electricity_Consumed < 200:
    charge_for_unit = 8
elif Electricity_Consumed >= 200:
    charge_for_unit = 12  
else:
    print('Enter a Valid Number of Units Power Consumed')  

service_charge = 80

Electricity_bill = service_charge + charge_for_unit*Electricity_Consumed


Total_month_bill = Rent_for_month + Utilities_bills + Groceries_bills + Electricity_bill

split_amount_per_person = Total_month_bill//num_of_people_living


print(f'Each person has to contribute amount of ₹ {split_amount_per_person} and the Total Amount for the month is {Total_month_bill}')
