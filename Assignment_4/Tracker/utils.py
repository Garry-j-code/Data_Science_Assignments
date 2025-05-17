import csv
from datetime import datetime
import os

def clear_screen():
    if (os.name == 'nt'):
        command = 'cls' 
    else:
       command = 'clear'
    os.system(command)

base_dir = os.path.dirname(os.path.dirname(__file__))  
db_path = os.path.join(base_dir, "data/records.csv")    