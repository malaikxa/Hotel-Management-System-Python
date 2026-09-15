from operator import truediv


def menu():
    print("========MENU=======")
    print("Press 1: calculate online store bill")
    print("Press 2: Employee info")
    print("Press 3: school attendance")
    print("Press 4: place restaurant order")
    print("Press 5: student report card")
    print("Press 6: Bank transaction logger")
    print("Press 7: University fee calculator")
    print("8: Exit")
def calculate_bill(*prices):
    total = sum(prices)
    print("Prices =", prices)
    print("Total Bill =", total)
def employee_info(**kwargs):
    print("Employee Information:")
    for key, value in kwargs.items():
        print(key,value)

def attendance(student_name,*days_present):
    print("Student Name:", student_name)
    print("Days Present:", days_present)
    print("Total Days Present =", len(days_present))

def  place_order(*items, **details):
    print("Items Ordered:", items)
    for key, value in details.items():
       print(key,value)

def report_card(name, status="Pass", **marks):
    print("Report Card", name)
    for sub, mark in marks.items():
        print(sub,mark)
    print("Status:", status)

def log_transaction(**transaction):
    print("Transaction Log:")
    for key, value in transaction.items():
        print(key,value)

def calculate_fee(base_fee, *extras, **concessions):
    total = base_fee + sum(extras) - sum(concessions.values())
    print("Base Fee:", base_fee)
    print("Extra Charges:", extras)
    print("Concessions:", concessions)
    print("Total Payable Fee =", total)
while True:
 menu()
 choice=int("Enter your choice")
 if choice==1:
     calculate_bill(290,980,450,110)
 elif choice==2:
     employee_info(name="yoshi",age=22,salary=10000)
 elif choice==3:
     attendance("denise","Mon","")








