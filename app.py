class Canteen:
    def __init__(self,cname):
        self.cname=cname
    
    def display(self):
        print(self.cname)

class Dishes:
    def __init__(self) -> None:
        pass
    def title(self):
        print("\n***Dishes Catelogue***")
    def VegList(self,i1,i2,i3,i4,i5):
        print("\n****1.Available Veg Foods****")
        print(i1)
        print(i2)
        print(i3)
        print(i4)
        print(i5)
    def NonVegList(self,i1,i2,i3,i4,i5):
        print("\n ****2.Available NonVeg Foods****")
        print(i1)
        print(i2)
        print(i3)
        print(i4)
        print(i5)
    def JuiceList(self,i1,i2,i3,i4,i5):
        print("\n ****3.Available Juices****")
        print(i1)
        print(i2)
        print(i3)
        print(i4)
        print(i5)

class UserChoice(Dishes):
    def __init__(self,choice):
        self.choice=choice
    
    def ChoiceCall(self):
        if (self.choice==1):
            Dishes.VegList()
        elif(self.choice==2):
            Dishes.NonVegList()
        else:
            Dishes.JuiceList()
        
       
# Canteen Manager Interface
name=Canteen("\n*****Ashwin's Canteen Management System*****")
name.display()
dishes=Dishes()
dishes.title()
dishes.VegList("1.Idly","2.Dosa","3.Sambar","4.Lemon Rice","5.Veg rice")
dishes.NonVegList("1.Biryani","2.Chicken Curry","3.Egg","4.Chicken Rice","5.Fish Fry")
dishes.JuiceList("1.Apple Juice","2.Oreo","3.Pine apple","4.Badam Gir","5.Lemon Juice")
