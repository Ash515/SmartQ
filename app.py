from unicodedata import category

from pathy import StreamableType
from pytz import AmbiguousTimeError
import os


def index():
    print("*********Smart Canteen System*********")
    regno = int(input("Enter your Register number:"))
    password = int(input("Enter your password:"))
    if (regno and password):
        authentication(regno, password)
    else:
        print("Please enter all the fields")


def authentication(regno, password):
    if (regno == 5005 and password == 2122):
        home()
    else:
        print("please enter correct credentials")


def home():
    print("\n Timings Schedule \n 1. 8.00 AM to 11.00 AM  \n 2. 11.30 PM to 3.00 PM  \n 3. 3.30 PM to 5.30 PM \n 4. 6.00 PM to 9.00 PM ")
    timings = int(input("\n Select your timings:"))
    if(timings == 1):
        Tiffen()
    elif(timings == 2):
        Lunch()
    elif(timings == 3):
        JuiceSnacks()
    elif(timings == 4):
        Tiffen()
    else:
        print("Please select proper time...")

def Tiffen():
    print("You have selected Fresh Juice and Snacks Category")
    print("Items... \n 1.Veg Pulav => 1 plate 50g $25  \n 2.Idly=> 1 pice $5 \n 3.Plain Dosa => 1 pice $20 \n 4. Parotta => 1 pice $10")
    DinnerChoice = input("Enter your Choice:")
    if(DinnerChoice == "1" or DinnerChoice == "Veg Pulav"):
        bill = QuantityCalc("Veg Pulav", 25)
        print("Your Total Bill Amount:", bill)
    elif(DinnerChoice == "2" or DinnerChoice == "Idly"):
        bill = QuantityCalc("Idly", 5)
        print("Your Total Bill Amount:", bill)
    elif(DinnerChoice == "3" or DinnerChoice == "Plain Dosa"):
        bill = QuantityCalc("Plain Dosa", 20)
        print("Your Total Bill Amount:", bill)
    elif(DinnerChoice == "4" or DinnerChoice == "Parotta"):
        bill = QuantityCalc("Parotta", 10)
        print("Your Total Bill Amount:", bill)
    else:
        print("Please choose a displayed foods")


def Lunch():
    print(" Please choose the categories:")
    print("\n Categories \n 1.Veg  \n 2.Non Veg \n 3.Fresh Juice")
    category = str(input("\nSelect your category(s):\n"))
    if(category == "1" or category == "Veg"):
        Veg()
    elif(category == "2" or category == "Non Veg"):
        NonVeg()
    elif(category == "3" or category == "Fresh Juice and Snacks"):
        JuiceSnacks()
    else:
        print("Please give a valid category in the list...")

def JuiceSnacks():
    print("You have selected Fresh Juice and Snacks Category")
    print("Items... \n 1.Lemon Juice => 1 glass 50ml $25  \n 2.Oreo Juice=> 1 glass 50ml $50 \n 3.Chicken Puffs => 1 glass 50g $20 \n 4. Chicken Roll => 1 glass 25g $10")
    juicesnacksChoice = input("Enter your Choice:")
    if(juicesnacksChoice == "1" or juicesnacksChoice == "Lemon Juice"):
        bill = QuantityCalc("Lemon Juice", 25)
        print("Your Total Bill Amount:", bill)
    elif(juicesnacksChoice == "2" or juicesnacksChoice == "Oreo Juice"):
        bill = QuantityCalc("Oreo Juice", 50)
        print("Your Total Bill Amount:", bill)
    elif(juicesnacksChoice == "3" or juicesnacksChoice == "Chicken Puffs"):
        bill = QuantityCalc("Chicken Puffs", 20)
        print("Your Total Bill Amount:", bill)
    elif(juicesnacksChoice == "4" or juicesnacksChoice == "Chicken Roll"):
        bill = QuantityCalc("Chicken Noodles", 10)
        print("Your Total Bill Amount:", bill)
    else:
        print("Please choose a displayed foods")


def Veg():
    print("You have selected Veg Category")
    print("Items... \n 1.Sambar Rice => 1 plate $30  \n 2.Veg Rice => 1 plate $40 \n 3.Lemon Rice => 1 plate $50 \n 4.Curd Rice => 1 plate 30Rs")
    VegItem = input("Enter your Choice:")
    if(VegItem == "1" or VegItem == "Sambar Rice"):
        price = 30
        bill = QuantityCalc("Sambar Rice", price)
        print("Your Total Bill Amount:", bill)
    elif(VegItem == "2" or VegItem == "Veg Rice"):
        bill = QuantityCalc("Veg Rice", 40)
        print("Your Total Bill Amount:", bill)
    elif(VegItem == "3" or VegItem == "Lemon Rice"):
        bill = QuantityCalc("Lemon Rice", 50)
        print("Your Total Bill Amount:", bill)
    elif(VegItem == "4" or VegItem == "Curd Rice"):
        bill = QuantityCalc("Curd Rice", 30)
        print("Your Total Bill Amount:", bill)
    else:
        print("Please choose a displayed foods")


def NonVeg():
    print("You have selected Non Veg Category")
    print("Items... \n 1.Chicken Rice => 1 plate $70  \n 2.Egg Rice => 1 plate $40 \n 3.Chicken Biryani => 1 plate $90 \n 4.Chicken Noodles => 1 plate $70")
    NonVegItem = input("Enter your Choice:")
    if(NonVegItem == "1" or NonVegItem == "Chicken Rice"):
        bill = QuantityCalc("Chicken Rice", 70)
        print("Your Total Bill Amount:", bill)
    elif(NonVegItem == "2" or NonVegItem == "Egg Rice"):
        bill = QuantityCalc("Egg Rice", 40)
        print("Your Total Bill Amount:", bill)
    elif(NonVegItem == "3" or NonVegItem == "Chicken Biryani"):
        bill = QuantityCalc("Chicken Biryani", 50)
        print("Your Total Bill Amount:", bill)
    elif(NonVegItem == "4" or NonVegItem == "Chicken Noodles"):
        bill = QuantityCalc("Chicken Noodles", 30)
        print("Your Total Bill Amount:", bill)
    else:
        print("Please choose a displayed foods")

def QuantityCalc(item, peramt):
    qty = int(input("Enter the quantity you want:"))
    billamt = qty*peramt
    print("********************Bill Details********************")
    print("Item Name:", item)
    print("You entered quantity:", qty)
    return billamt

index()