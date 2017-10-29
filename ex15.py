from sys import argv 
#get "argument" feature from the huge "system" package.

script, filename = argv 
#call out variables named "script" , " filename".

txt = open(filename) 
# open is the command that return our file to something called "file objects".
# "File object" likes a DVD player,my file is like a CD
# with "File object", i can play, delete, rewrite,... my "CD". 

print "Here's your file %r: " %filename
print txt.read()
# txt is a variable or an object and the dot "." must be here
# to add a command "read". The command "read" is.

print "Type the filename again: " 
file_again = raw_input('> ')
# after typing a name of file,for example "ex15_sample.txt"
# the command "raw_input" will read my file.
# (other files (not ex15_sample.txt) can work, 
#   I have tested with "ex15test.docx)

# ask user to type the file name again.
txt_again = open(file_again)
# -"give" the file to the variable "txt_again" by the command "open"
#  and use it in the next line below.
# -open() : file objects must be inside the parentheses ()
#  because if I use open(" >"), it'll be a foul.

print txt_again.read()
# again,if I want to do something with a file, I need a dot "."
# and a command after the dot.

txt.close()
txt_again.close()
# Zed asked me to close files when I'm done with them :)).
# I think it's very necessary.
