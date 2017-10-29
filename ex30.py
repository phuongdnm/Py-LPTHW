people = 300
cars = 40
buses = 50


if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We shouldn't not take the cars."
else:
	print "We can't decide."

if buses > cars:
	print "That's too many buses."
elif buses < cars:
	print "Maybe we could take the buses."
else:
	print "We still can't decide."

if people > buses:
	print "Alright, let's just take the buses."
else:
	print "Fine, let's stay home then."

if cars > people and buses < cars:
	print "Cars> people and buses < cars."
elif cars > people and buses == cars:
	print "Cars > people and buses = cars."
elif cars < people and buses < cars:
	print "Cars < people and buses < cars."
elif cars < people and buses == cars:
	print "Cars < people and buses = cars."
else:
	print "Nothing true :(("

# IMPORTANT: If multiple "elif" blocks are True, Python will run ONLY
# the first one. For example:
if people > cars and buses > cars:
	print "Only this line will be printed."
elif people > buses:
	print "This line won't be printed."
elif cars <= buses :
	print "This line won't neither."
else:
	print "Or I'm wrong."

