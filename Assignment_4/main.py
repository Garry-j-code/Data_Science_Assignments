import csv
from Tracker.utils import *
from Tracker.transactions import addTransaction
from Tracker.tracker import financialReport

check = True

while(check):
    clear_screen()
    print("Welcome to My Porject")

    print("Press 1 to Add Transaction")
    print("press 2 to check Financial Report")
    print("Press Any other key to exit")

    choice = (input("\nEnter your choice: "))

    if(choice == '1'):
        choice2 = True
        while(choice2):
            addTransaction()
            print("Transaction added successfully")
            anotherTransaction = str(input("Do you want to add another transaction?(yes/no): ")).strip()
            anotherTransaction = anotherTransaction.lower()
            print(anotherTransaction)
            if(anotherTransaction == "no"):
                choice2 = False
            else:
                clear_screen()
    elif(choice == '2'):
        # print("This is option 2")
        financialReport()
        input("\n\nPress any key to proceed")
    else:
        check = False 