import sys
import uuid
from datetime import datetime
from Tracker.utils import *

def addTransaction():
    idOfTransaction = uuid.uuid4().hex
    while True:
        try:
            amount = int(input("\nPlease Enter the amount of the Transaction: $"))
            break
        except ValueError:
            print("Error: Please enter the amount in digits only")

    
    while True:
        try:
            typeOfTransacton = str(input("Please Enter the type of Transaction(Income/Expense): ")).strip()
            typeOfTransacton = typeOfTransacton.lower()
            typeOfTransacton = typeOfTransacton.capitalize()
            if(typeOfTransacton != ('Income' or 'Expense' )):
                raise ValueError
            break
        except ValueError:
            print("Error: Please enter only Expense or Income")
    
    

    if(typeOfTransacton == 'Expense'):
         category = str(input("Please Enter the type of Expense from any of the below types: \nGrocery || Online Shoping || Pharmacy || Electricty Bill || Water Bill || Other: ")).strip()
         category  = category.lower()
         category = category.title()
    else:
        category = ''

    timeOfTransaction = datetime.now() 
    transaction = [idOfTransaction, amount, typeOfTransacton, category, timeOfTransaction]

    try: 
        with open(db_path,"a+") as f:
            wo = csv.writer(f, delimiter=',')
            wo.writerow(transaction)
    except FileNotFoundError:
        print("Error: Not able to find the file in Database")
        raise SystemExit()