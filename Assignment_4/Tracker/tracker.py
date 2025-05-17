from Tracker.utils import *

def financialReport():
   
    with open(db_path,"r") as f:
        ro = csv.reader(f, delimiter=',')
        
        data = list(ro)
        for ele in data:
            if(ele[2] == 'Expense'):
                print(f"{ele[3]}: {ele[1]}")