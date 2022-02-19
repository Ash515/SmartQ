class Canteen:
    def __init__(self, cname):
        self.cname = cname

    def display(self):
        print(self.cname)


# class Dishes:
#     def __init__(self) -> None:
#         pass

#     def title(self):
#         print("\n***Dishes Catelogue***")

#     def VegList(self, i1, i2, i3, i4, i5):
#         print("\n****1.Available Veg Foods****")
#         print(i1)
#         print(i2)
#         print(i3)
#         print(i4)
#         print(i5)

#     def NonVegList(self, i1, i2, i3, i4, i5):
#         print("\n ****2.Available NonVeg Foods****")
#         print(i1)
#         print(i2)
#         print(i3)
#         print(i4)
#         print(i5)

#     def JuiceList(self, i1, i2, i3, i4, i5):
#         print("\n ****3.Available Juices****")
#         print(i1)
#         print(i2)
#         print(i3)
#         print(i4)
#         print(i5)


# class UserChoice(Dishes):
#     def __init__(self, choice):
#         self.choice = choice

#     def ChoiceCall(self):
#         if (self.choice == 1):
#             Dishes.VegList()
#         elif(self.choice == 2):
#             Dishes.NonVegList()
#         else:
#             Dishes.JuiceList()


class ManagerDishEnteryChoice():
    def __init__(self, choice):
        self.choice = choice

    def DishEntry(self, itemCount):

        vegList = {}
        nonvegList = {}
        juiceList = {}
        if self.choice == 1:

            i = 0
            while (i < itemCount):
                item1 = input("Enter Item 1:")
                item1Amt = int(input("Enter the amount for item1"))
                vegList[item1] = item1Amt
                i += 1
        elif(self.choice == 2):

            i = 0
            while (i < itemCount):
                item2 = input("Enter Item 2:")
                item2Amt = int(input("Enter the amount for item2"))
                nonvegList[item2] = item2Amt
                i += 1
        else:

            i = 0
            while (i < itemCount):
                item3 = input("Enter Item 3:")
                item3Amt = int(input("Enter the amount for item3"))
                juiceList[item3] = item3Amt
                i += 1
        print("\n***Dishes***")
        for k,v in vegList.items:
            print("Item Name:",k,"Item Amount:",v)
        for k,v in nonvegList.items:
            print("Item Name:",k,"Item Amount:",v)
        for k,v in juiceList.items:
            print("Item Name:",k,"Item Amount:",v)
        


# Canteen Manager Interface
nameEntry = input("Enter the canteen name:")
Cname = Canteen(nameEntry)
Cname.display()
status = int(input("Do you want to entry the new Items 1.Yes  2.No"))
if status == 1:
    item = int(input("1.Veg 2.Non Veg 3.Juice"))
    if item == 1:
        vegentry = ManagerDishEnteryChoice(1)
        itemCnt = int(input("How many Items:"))
        vegentry.DishEntry(itemCnt)
    elif(item == 2):
        nonvegentry = ManagerDishEnteryChoice(2)
    else:
        juiceentry = ManagerDishEnteryChoice(3)
else:
    print("not selected ")


# dishes.VegList("1.Idly","2.Dosa","3.Sambar","4.Lemon Rice","5.Veg rice")
# dishes.NonVegList("1.Biryani","2.Chicken Curry","3.Egg","4.Chicken Rice","5.Fish Fry")
# dishes.JuiceList("1.Apple Juice","2.Oreo","3.Pine apple","4.Badam Gir","5.Lemon Juice")
