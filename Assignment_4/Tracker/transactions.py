import uuid
from datetime import datetime
from Tracker.utils import *

def addTransaction():
    amount = int(input("\nPlease Enter the amount of the Transaction: $"))
    idOfTransaction = uuid.uuid4().hex
    typeOfTransacton = str(input("Please Enter the type of Transaction(Income/Expense): ")).strip()
    typeOfTransacton = typeOfTransacton.lower()
    typeOfTransacton = typeOfTransacton.capitalize()

    if(typeOfTransacton == 'Expense'):
         category = str(input("Please Enter the type of Expense from any of the below types: \nGrocery || Online Shoping || Pharmacy || Electricty Bill || Water Bill || Other: ")).strip()
         category  = category.lower()
         category = category.title()
    else:
        category = ''

    timeOfTransaction = datetime.now() 
    transaction = [idOfTransaction, amount, typeOfTransacton, category, timeOfTransaction]

    with open(db_path,"a+") as f:
        wo = csv.writer(f, delimiter=',')
        wo.writerow(transaction)