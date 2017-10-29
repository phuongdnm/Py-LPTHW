tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split \non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#1
print "%s" % "\n" *5
print "Now I gonna test some ESCAPE SEQUENCES"
print " Minh \\ Phuong . " # this is \\ means only one \ appears
print " Minh \' Phuong . " # this is \' means only ' appears
print " Minh \" Phuong ."  # same the previous line
print " Minh \a Phuong. "  # ASCII Bell, it will let you hear the SYSTEM SOUND 
print " Minh \b Phuong. "  # ASCII backspace, I don't know how it works :((
print " Minh \t Phuong. "  # means Tab
print " Minh \ Phuong."    # the same as \\,why???

#2
print "%s" % "\n" 
#piece of funny code to try out:
#while True:
#	for i in ["/", "-", "|", "\\", "|"] :
#		print "%s \r " %i,
		
#3: use '''
print '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip \n \t* Grass
''' #they are in the same as """
