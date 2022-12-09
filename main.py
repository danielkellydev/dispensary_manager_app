import pandas as pd
import os
import formulas
clear = lambda: os.system('cls')


def menu():
    clear()
    print("============= Dispensary Manager ============")
    print ('')
    while (1):
        print("1) Display full dispensary inventory")
        print("2) Display low stock items")
        print("3) Update herb inventory")
        print("4) Prescribe formula")
        print("5) Exit/Go back")
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
    df= pd.read_csv('inventory.csv')
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
    
    df = df= pd.read_csv('inventory.csv')
    low_herbs = df[(df['Grams'] < 100)]
    print (low_herbs)
    print ('')
    print ('')

def update_herbs():
    clear()
    while True:
        df = pd.read_csv('inventory.csv', index_col='Herb')
        df_to_list= pd.DataFrame(df).index.tolist()
        
        herb_to_change= input("Herb to update: ")
        
        if herb_to_change in df_to_list:
            new_grams= input("Enter updated grams: ")
            df.loc [herb_to_change, 'Grams'] = new_grams
            df.to_csv("inventory.csv")
        elif herb_to_change == '5':
            break
        else:
            print("Incorrect input!")
            
        
       
def prescribe():
    df = pd.read_csv('inventory.csv', index_col='Herb')
    df_to_list= pd.DataFrame(df).index.tolist()
    for i in formulas.li_zhong_wan:
        if i in df_to_list:
            df.loc [i, 'Grams'] = (df.loc [i, 'Grams']) - (formulas.li_zhong_wan[i])
            df.to_csv("inventory.csv")

clear()
menu()