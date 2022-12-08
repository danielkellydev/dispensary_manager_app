import pandas as pd
import os
clear = lambda: os.system('cls')

dispensary_items = { 
                "Herb": ["bai zhu", "fu ling", "zhi gan cao", "huang qin", "fu zi", "huang lian", "gan jiang", "ren shen", "ban xia", "bai shao", "gui zhi", "da zao"],
                "Grams": [324, 220, 110, 90, 65, 454, 245, 500, 600, 300, 200, 250]
                    }






def menu():
    clear()
    print("============= Dispensary Manager ============")
    print ('')
    while (1):
        print("1) Display full dispensary inventory")
        print("2) Display low stock items")
        print("3) Update herb inventory")
        print("4) Prescribe formula")
        print("5) Exit")
        print('')
        print("Enter Your Choice :- ")

        n = int(input())
        if (n == 1):
            display_herbs()
        elif(n == 2):
            display_low_herbs()
        elif(n == 3):
            update_herbs()
        elif(n == 4):
            prescribe()
        elif (n == 5):
            break
        else:
            print("Invalid Choice, please try again")

def display_herbs():
    clear()
    df = pd.DataFrame.from_dict(dispensary_items)
    print('')
    print('')
    print('Full Inventory')
    print('--------------')
    print(df)
    print('')

def display_low_herbs():
    clear()
    print ('')
    print("Low Stock Items")
    print("---------------")
    print ('')
    
    df = pd.DataFrame.from_dict(dispensary_items)
    low_herbs = df.loc[df["Grams"] <100]
    print (low_herbs)
    print ('')
    print ('')

def update_herbs():
    pass

def prescribe():
    pass

menu()