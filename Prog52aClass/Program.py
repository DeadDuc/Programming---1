class rectangle:
	def __init__(self, length, width): # Constructor
		self.length = length
		self.width = width
		
	def area(self): # Class function
		return self.length * self.width
	
	def perimeter(self):
		return self.length * 2 + self.width * 2
	
	
length = int(input("Enter length: "))
width = int(input("Enter width: "))
r = rectangle(length, width) # Call class constructor to make new instance
print("Area:", r.area())
print("Perimeter:", r.perimeter())

input()