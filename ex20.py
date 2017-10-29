### IMPORTANT: - The example file is "ex20_sample.txt"
###			   - I have done the very EXCITING study drill 5 also :))
from sys import argv

script, input_file = argv

def print_all(f):
# Creat a function named "print_all" with varialbe "f".
	print f.read()
# Read variable "f".

def rewind(f): 
# "rewind" means make something go backwards.
	f.seek(0)
# - This is how "seek" command works: f.seek(offset,from_what).
# - "offset" means how many bytes (positions) I will move.
# - "from_what" defines where is my pointer:
#	+ 0: means my reference point is the BEGINING of the file.
#**	+ 1: means my reference point is the CURRENT file position,for example:
#		go to my "ex20_sample.txt" and CLICK RANDOMLY at the text,then run:
#			f.seek(3,1) : for now, I failed :((
#	+ 2: means my reference point is the END of the file.
# - For example, run this line instead of line 12, I will see the difference:
#1 	f.seek(15,0)
#2	f.seek(20,1)
#3  f.seek(-5,2)


def print_a_line(line_count, f):
# There are 2 variables in this function: "line_count" and "f"
	print line_count, f.readline()
### - The "readline(x)" command only read one line, then "jump down"
### to next line.
### - It means python will read my string until it hits a new line. 

	
current_file = open(input_file)

print "First let's print the whole file: \n"

print_all(current_file)
# - This line is equal to: print_all(open(input_file))
# - Run function "print_all" with varialbe "current_file" which is
# the file object of "input_file"

print "Now let's rewind, kind of like a tape."

rewind(current_file)
# Instead of close the "input_file", this command take the pointer to the
# begining of the file.

print "Let's print three lines: "

current_line =1
# Make a global variable name "current_line" with value 1.
print_a_line(current_line, current_file)
# - "current_line" is now the "line_count" and = 1
# - "current_file" is "f", but python will read only the FIRST line
# because of the "readline" command, then "jump down" to the SECOND line
# but won't read this line. 

####### STUDY DRILL 5: use the shorthand notation +=
#current_line = current_line  + 1
current_line += 1
####### for example: "x += 1" is equal to " x = x + 1"
print_a_line(current_line, current_file)
# And now, the pointer is at the begining of the SECOND line, "current_file"
# will be read at this line only and then "jump down" again :)) 

current_line += 1
print_a_line(current_line, current_file)
# Finally, the pointer is at the begining of the THIRD line, it do the same
# as I said in lines 60 and 61.

# I can test what I have said with these lines:
# current_line = current_line +1 
# print_a_line(current_line, current_file)
# =====> It shows only number "4" because my text has 3 lines :))


