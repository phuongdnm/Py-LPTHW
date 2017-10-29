print "-"*10
print "Nam xxx thuoc the ki nao?"
print "-"*10

def the_ky(nam):
	if (nam % 100) == 0:
		the_ky = nam / 100
	else:
		the_ky = nam / 100 + 1
	return the_ky

print "Ban can tim nam nao?"
nam = int(raw_input("> "))
print the_ky(nam)

# CODE FIGHTS: 
"""
def century_calculation(year):
	return (year + 99) // 100

