name = "Zed A.Shaw"
age = 35 #not a lie
height = 74 #inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d centimeters tall." % (height*2.54)
print "He's %r kilos heavy." % (weight*0.45)
print "Actually that's not too heavy."
print "He's got %r eyes and %r hair." % (eyes, hair)
print "His teeth are usually %r depending on the coffee." % teeth

#this line is tricky, try to get it exactly right
print "If I add %r, %r, and %r I get %r." % (	
	age, height, weight, age + height + weight
	)
	