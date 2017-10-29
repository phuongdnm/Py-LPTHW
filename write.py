### IMPORTANT : -In this programe, the example file is named "ex16_sample.txt"
### - I also create a programe name "ex16sd2.py" to read the file below
### - In this programe, I have done the study drill 2 that asked me 
### to shorter the part : target.write(). I done it by 2 ways below.

from sys import argv
# As usual, get the "argv" feature from the "system" package.

script , filename = argv
# Call out some variables from argument "library"

print "We're going to erase %r. " % filename
print "If you don't want that,hit CTRL-C (^C). "
print "If you do want that, hit RETURN or Enter."

raw_input("?") 
# Wait a minute, this line just pause the programe for a while
# to ask people if they want to continue or quit.

print "Opening the file..."
target = open(filename, 'w')
# This "open" command consist of 2 parts: 
# open("filename, "mode").
# "w" means "write". 
# There are "r","w", "a", "r+".

print "Truncating the file. Goodbye!"
#target.truncate()
#1 Python automatically truncates files when I'm in "w" - write mode.
#1 So I don't need this line :))  

#2 AS I know, if I want to do something with my file
#2 I'll put a dot "." and the command after the dot.
#2 "truncate" command: empties the file.

print "No I'm going to ask you for three lines."
# ask user to type some fucking line that they want to put in
# the file ex16_sample.txt.

line1 = raw_input("line 1: ") # the system read the "input".
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

#0 target.write(line1) 
	#0 -Now I know how it work:
	#0 target file + the dot "." + the command.
	#0 -But in this "write" command,
	#0  there is a string "line1" inside the perenthesis.
#0 target.write("\n")
#0 target.write(line2)
#0 target.write("\n")
#0 target.write(line3)
#0 target.write("\n")

#1 target.write(line1 + "\n"+ line2 + "\n"+ line3)
	#1 This one is my thought :)) Instead of 6 lines,i need only 1 line. 

target.write("{0}\n{1}\n{2}\n".format(line1,line2,line3))
# This is the code i searched from Stackoverflow. It's so crazy :)) 

print "And finally, we close it."
target.close()


               