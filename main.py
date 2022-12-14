import pandas as pd
import os
import formulas
clear = lambda: os.system('cls')

# function for displaying menu
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

        # error handling in case a non-integer is inputted
        try:
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
        except ValueError:
            print ('')                  
            print("--------------------------------")
            print("Invalid Choice, please try again.")
            print("--------------------------------")
            print('')

# function to print full inventory from csv file
def display_herbs():
    clear()
    df= pd.read_csv('./inventory.csv')
    print('')
    print('')
    print('--------------')
    print('Full Inventory')
    print('--------------')
    print(df.to_string (index=False))
    print('')

# function to display any herbs in the dispensary whose grams is below 100
def display_low_herbs():
    clear()
    print ('')
    print("---------------")
    print("Low Stock Items")
    print("---------------")
    print ('')
    
    #uses pandas to read csv file, then recognises any herbs below 100 
    df= pd.read_csv('./inventory.csv')
    low_herbs = df[(df['Grams'] < 100)]
    # if the dataframe is empty, a friendly message is displayed (as opposed to default empty dataframe message)
    if low_herbs.empty:
        print ('')
        print ("You're all stocked up!")
        print ('')
    else:
        print(low_herbs.to_string (index=False))
        print ('')
        print ('')

# function to edit grams value of herbs in csv file
def update_herbs():
    clear()
    print('Main Menu (5)')
    print('')
    while True:
        # using pandas to read csv
        df = pd.read_csv('./inventory.csv', index_col='Herb')
        # transpose csv data into a pandas DataFrame, then into a list
        df_to_list= pd.DataFrame(df).index.tolist()
        
        herb_to_change= input("Herb to update: ")
        herb_to_change= herb_to_change.capitalize()
        
        # if loop checks if above herb_to_change input is located within the df_to_list list
        if herb_to_change in df_to_list:
            new_grams= input("Enter updated grams: ")
            df.loc [herb_to_change, 'Grams'] = new_grams
            df.to_csv("./inventory.csv")
            print ('')
            print(f"{herb_to_change.capitalize()} updated to {new_grams} grams.")
            print ('')
        elif herb_to_change == '5':
            clear()
            break
        else:
            print("Incorrect input!")
            
        
    #    function to prescribe herbal formulas
def prescribe():
    df = pd.read_csv('./inventory.csv', index_col='Herb')
    formula = ''
    clear()
    print('')
    print('------------')
    print('Formula Menu')
    print('------------')
    print('')
    print("1) Li Zhong Wan")
    print("2) Ban Xia Xie Xin Tang")
    print("3) Zhen Wu Tang")
    print("4) Fu Zi Tang")
    print("5) Ling Gui Zhu Gan Tang")
    print("6) Shen Zhuo Tang")
    print("7) Da Xuan Wu Tang")
    print("Formula to prescribe :- ")
# error handling in case a non-integer is inputted
    try: 
        n = int(input())
        if (n == 1):
            formula= formulas.lzw
            formula_name = 'Li Zhong Wan'
        elif(n == 2):
            formula= formulas.bxxxt
            formula_name = 'Ban Xie Xie Xin Tang'
        elif(n == 3):
            formula= formulas.zwt
            formula_name = 'Zhen Wu Tang'
        elif(n == 4):
            formula= formulas.fzt
            formula_name = 'Fu Zi Tang'
        elif (n == 5):
            formula= formulas.lgzgt
            formula_name = 'Ling Gui Zhu Gan Tang'
        elif (n == 6):
            formula= formulas.szt
            formula_name = 'Shen Zhuo Tang'
        elif (n == 7):
            formula= formulas.dxwt
            formula_name = 'Da Xuan Wu Tang'
        else:
            print ('')                  
            print("--------------------------------")
            print("Invalid Choice, please try again.")
            print("--------------------------------")
            print('')
    except ValueError:
            print ('')                  
            print("--------------------------------")
            print("Invalid Choice, please try again.")
            print("--------------------------------")
            print('')
    
    print ('')
    print ('')
    

# this code takes the values of individual herbs within prescribed formula, checks them against same herb names in
# inventory.csv, and then deducts values
    count= 0
    df_to_list= pd.DataFrame(df).index.tolist()
    for i in formula:
        if i in df_to_list:
            if (df.loc [i, 'Grams']) < (formula[i]):
                clear()
                print ("Herb stocks are too low to prescribe that formula, please check low stock items and restock as needed.")
                print ('')
                break
            else:
                formula_length= len(formula)
                df.loc [i, 'Grams'] = (df.loc [i, 'Grams']) - (formula[i])
                df.to_csv('./inventory.csv')
                count += 1
                # used a counter to only display confirmation message once all herbs in a formula are complete
                if count == formula_length:
                    clear()
                    print (f'{formula_name} successfully prescribed')
                    print ('')

menu()