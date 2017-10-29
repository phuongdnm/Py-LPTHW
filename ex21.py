def add(a, b):
	print "ADDING %d + %d " % (a, b)
	return a + b 

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b
	
def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b
	

print "Let's do some math with just function!"

x = int(raw_input("x= "))
y = int(raw_input("y= "))
# It's very important to use int() command.
age = add(x, y)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)


print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzzle for extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq,2))))
# - When I run the script, here're the result:
#     DIVIDING 50 / 2
#     MULTIPLYING 180 * 25
#     SUBTRACTING 74 - 4500
#     ADDING 9 + -4426
# - It means: Python print the fomula "backward".
# ("backward" means from inside to outside, in this situation, python
# do the math from "divide" to "add")

print "That becomes: ", what, "Can you do it by hand?"

