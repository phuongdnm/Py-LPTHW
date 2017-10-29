def displaysum(a,b):
	print "So a la: %d" % a
	print "So b la: %d" % b
	print "====> Tong la : %d" % (a+b)
	print "Xuong dong. \n"

#1: put number directly
print "#1:"
displaysum(23,10)

#2: use variables
print "#2:"
x= 5
y= 7
displaysum(x,y)

#3: doing math is ok!
print "#3:"
displaysum(5+6,8+9)

#4: using both variables and math
print "#4:"
displaysum(x+10,y+10)

#5: ask user for 2 input numbers
print "#5:"
var1 = int(raw_input("n1= "))
var2 = int(raw_input("n2= "))
displaysum(var1,var2)

#6***: Function in function
def bigger_function():
	x1 = 100
	x2 = 200
	displaysum(x1,x2)

print "#6:"
bigger_function()

#7: use argument
print "#7:"
phuong = (15,20)
displaysum(*phuong)



