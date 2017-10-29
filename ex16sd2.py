from sys import argv

script, filename = argv

txt = open(filename)

print "Here're the text in the file %s: " % filename
print "\n"
print txt.read()
print "\n"
print "That's great,congratulations."

txt.close()