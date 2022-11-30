import numpy as np
from os import system, name

def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
        
def task_1():
    print("not ready")
    print("Type smth to move next" )
    input()
    
def task_2():
    print("not ready")
    print("Type smth to move next" )
    input()

def task_3():
    print("not ready")
    print("Type smth to move next" )
    input()

def task_4():
    print("not ready")
    print("Type smth to move next" )
    input()

def task_5():
    print("not ready")
    print("Type smth to move next" )
    input()

def task_6():
    print("not ready")
    print("Type smth to move next" )
    input()

switcher = 0
while int(switcher) <= 7:
    clear()
    print("1. Task 2.1")
    print("2. Task 2.2")
    print("3. Task 2.4")
    print("4. Task 3.1")
    print("5. Task 5.1")
    print("6. Task 6.2")
    print("7. Exit")
    print("Please, select number from 1 to 7:")
    switcher = input()
    clear()

    if   int(switcher) == 1:
        task_1()
    elif int(switcher) == 2:
        task_2()
    elif int(switcher) == 3:
        task_3()
    elif int(switcher) == 4:
        task_4()
    elif int(switcher) == 5:
        task_5()
    elif int(switcher) == 6:
        task_6()
    elif int(switcher) == 7:
        break