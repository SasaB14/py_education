#problem1
class Line:

	def __init__(self,coor1,coor2):
		self.coor1 = coor1
		self.coor2 = coor2

	def distance(self):
		x1,y1 = self.coor1
		x2,y2 = self.coor2
		return ((x2-x1)**2 + (y2-y1)**2)**0.5

	def slope(self):
		x1,y1 = self.coor1
		x2,y2 = self.coor2
		return (y2-y1)/(x2-x1)

# EXAMPLE OUTPUT
coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
print(li.distance())
print(li.slope())


#problem2
class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return 3.14*self.height*(self.radius)**2
    
    def surface_area(self):
        return ((2*3.14*self.radius*self.height)+(2*3.14*(self.radius**2)))

# EXAMPLE OUTPUT
c = Cylinder(2,3)
print(c.volume())
print(c.surface_area())


print('\n')

##Challenge
class Account:

	def __init__(self,owner,balance):
		self.owner = owner
		self.balance = balance

	def __str__(self):
		return "Account owner: %s, \nAccount balance: %s" %(self.owner, self.balance)

	def deposit(self,dodatak):
		self.balance = self.balance + dodatak

	def withdrawal(self,skidanje):
		if skidanje <= self.balance:
			self.balance = self.balance - skidanje
			print("na racunu je ostalo %s."%(self.balance))
		else:
			print("na racunu je %s ne mozete da povucete %s"%(self.balance,skidanje))



acct1 = Account('Jose',100)
print(acct1)
print(acct1.owner)
print(acct1.balance)
acct1.deposit(50)
print("\nposle dodavanja 50 stanje je:")
print(acct1.balance)
acct1.withdrawal(75)
acct1.withdrawal(750)
