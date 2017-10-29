from sys import argv

script, first, second, third = argv
fourth = raw_input("What's your fourth variable?")

print """
	Your script name is %s, 
	the first varialbe is %s, 
	the second variable is %s, 
	the third is %s
	the fourth %s """ %(script, first, second, third, fourth)