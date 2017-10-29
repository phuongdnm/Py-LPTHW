from sys import argv

script, filename = argv

print "Here're your file '%s': " % filename;
print "\n"

print open(argv[1]).read()

print "\n"
print "That's ok? Congratulations."

