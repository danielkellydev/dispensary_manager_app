# Dispensary Manager (Beta)

Author: Daniel Kelly<br>
danielkellydev@gmail.com<br>

Repository Link: https://github.com/danielkellydev/dispensary_manager

Display Manager is an application to assist herbalists in managing their herbal dispensary. At this point in time, there is included a small dispensary of 12 herbs, though in later versions there will be a feature to add new herbs to the dispensary. 

## App Features
<br>

### *Display full dispensary inventory*
Simply display the full list of herbs in the dispensary, and the current amount of grams. 

### *Display low stock items*
Rather than looking through the entire dispensary of herbs to check stock levels, you can use this function to single out all herbs that are under 100 grams. 

### *Update herb inventory*
When you do stock up herb inventories, this is the function you will use to record the new amounts of grams of a given herb. 

### *Prescribe Formula*
When you select a formula from the list to prescribe, the grams of the individual herbs will be deducted from the inventories, and hence provides an automated way to update herb inventories when formulas are prescribed. 

## App Implementation Plan

<br>

The implementation plan was created on an online platform called Asana. It can be accessed via the below link:

https://app.asana.com/0/1203497138825323/list

<br>

![asana image1](/terminal_app_assig\docs\asana1.jpg)<br>
![asana image2](/terminal_app_assig\docs\asana2.jpg)<br>
![asana image3](/terminal_app_assig\docs\asana4calendar.jpg)


## Operating Instructions

### *Running the app*
Ensure terminal is in correct directory, then use the command `./run.sh` to start the app. Using the app does require the Pandas module, which installs automatically by running the run.sh executable. 

### *Menu*
The menu is navigated by entering the number index values. 

![menu](/terminal_app_assig\docs\menu.jpg)
For example, enter `1` and press Enter to Display full dispensary inventory. 


## *Using the Features*
### *1) Display full dispensary inventory &* 
### *2) Display low stock items*
Not much instruction is needed for the first two options. Once these options are called, they simply display the requested data. To exit, press 5 and then Enter. 
![inventory_image](/terminal_app_assig\docs\inventory.jpg)

![low_stock_image](/terminal_app_assig\docs\lowstockitems.jpg)

If there are no low stock herbs in the inventory, the app will indicate this by letting you know 'You're all stocked up!' 

![low_stock_image](/terminal_app_assig\docs\lowstockitems2.jpg)



### *3) Update herb inventory*

