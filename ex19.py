# IMPORTANT: - My own function I do in study drill 3 named: ex19sd3.py

def cheese_and_crackers(cheese_count, boxes_of_crackers):
# The opening of the function : def + function's name + (arg1 ,arg2):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket. \n"
# These lines have nothing to say.

print "We can just give the function numbers directly"
cheese_and_crackers(20, 30)
# OR cheese_and_crackers("dinh_nhu", "minh_phuong")
# - The first way to "run" a function: use number or string directly.
# - But remember: In line 2 and 3 of the function, I use %d, so if I want to
# print strings, i need to change to %r instead.

print "OR, we can use varialbes forom our script: "
amount_of_cheese = 10
amount_of_crackers = 50
# Two GLOBAL VARIABLES, try not to use them because of the hard managing.

cheese_and_crackers(amount_of_cheese, amount_of_crackers)
# The second way to "run" a function: use varialbe.

print "We can even do math indise too:"
cheese_and_crackers( 10+20, 5+6)
# The third way to "run" a function: I can do math!

print "And we can combine the two, varialbes and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers +1000)
# The fourth way to "run" a function: I can use both varialbe and math.
