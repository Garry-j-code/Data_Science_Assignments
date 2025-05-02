import os

def addDataIntoDatabase():
    n = int(input("Please enter how many records you want to eneter: "))
    while(n):
        name = str(input("\nPlease enter user's Name: "))
        name = "Name: " + name
        phone = str(input("Please enter user's Phone Number: "))
        phone = "Phone: " + phone
        email = str(input("Please enter user's Email Address: "))
        email = "Email: " + email
        group = str(input("Please enter user's Group: "))
        group = "Group: " + group
        userData = [name, phone, email, group]

        HERE = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(HERE, "mainDatabase.text")

        with open(db_path,"a+") as f:
            f.write("\n")
            for item in userData:
                f.write(f"{item}\n")

        n -= 1

def searchRecordsViaName():
    nameNeedToFind = str(input("Enter the Name that we need to find in Database: "))
    nameNeedToFind = "Name: " + nameNeedToFind
    
    HERE = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(HERE, "mainDatabase.text")
    counter = 1
    
    with open(db_path,"r") as f:
        for line in f:
            line  = line.strip("\n")
            if(line == nameNeedToFind or counter > 1):
                print(line)
                counter += 1
            if(counter == 5):
                counter = 1
    
    input("\nPress any key to continue: ")

def searchRecordsViaGroup():
    nameNeedToFind = str(input("Enter the Group that we need to find in Database: "))

    HERE = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(HERE, "mainDatabase.text")
    users = []
    with open(db_path,"r") as f:
        record = {}
        for line in f:
            line = line.strip()
            if not line:
                if record:
                    users.append(record)
                    record = {}
            else:
                key, value = line.split(": ", 1)
                record[key] = value
        if record:
            users.append(record)
    
    for ele in users:
        if ele["Group"] == nameNeedToFind:
            print(ele)

def deleteRecords():
    needToDelete = str(input("Enter the Email address of the user who's record needs to be deleted: "))

    HERE = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(HERE, "mainDatabase.text")
    users = []
    with open(db_path,"r") as f:
        record = {}
        for line in f:
            line = line.strip()
            if not line:
                if record:
                    users.append(record)
                    record = {}
            else:
                key, value = line.split(": ", 1)
                record[key] = value
        if record:
            users.append(record)
    
    filtered_Data = []

    for user in users:
        if user["Email"] != needToDelete:
            # print("Inside if\n")
            # print()
            filtered_Data.append(user)
            # filtered_Data.append("\n")

    if len(users) == len(filtered_Data):
        print(f"This {needToDelete} is not present in the current Database")

    with open(db_path,"w") as f:
        f.write("\n")
        for user in filtered_Data:
            for key in user:
                f.write(f"{key}: {user[key]}\n")
            if user != users[-1]:
                f.write("\n")

    print(f"Record with Email = {needToDelete!r} deleted successfully.")

check = True
while(check):
    print("\nWelcome to my Data ingestion program")
    print("Press 1 to add the records in the database")
    print("Press 2 to Search the records via Name")
    print("Press 3 to Search the records via Group")
    print("Press 4 to Delete the records from the database")
    print("Press 5 to Close the Program")

    choice = int(input("\nEnter your choice: "))

    if(choice == 1):
         addDataIntoDatabase()
    elif(choice == 2):
        searchRecordsViaName()
    elif(choice == 3):
        searchRecordsViaGroup()
    elif(choice == 4):
        deleteRecords()
    elif(choice == 5):
        check = False