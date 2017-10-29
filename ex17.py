### IMPORTANT: -Example file are "ex17old.txt" and "ex17new.txt"
###			   -Change "ex17old.txt" by using ex16.py or using command "echo"
###			   -Read the content of the file by using command "cat" or "more"

#0 THIS IS THE MAIN CODE BY ZED...
#0 from sys import argv
#0 #from os.path import exists
#0 
#0 script, from_file, to_file = argv
#0 
#0 #print "Copying from %s to %s" % (from_file, to_file)
#0 
#0 #we could do these two on one line too, how?
#0 in_file = open(from_file)
#0 indata = in_file.read()
#0 
#0 #print "The input file is %d bytes long" % len(indata)
#0 
#0 #print "Does the output file exist? %r" % exists(to_file)
#0 #print "Ready, hit RETURN to contunue, CTRL-C to abort."
#0 #raw_input()
#0 
#0 out_file = open(to_file, 'w')
#0 out_file.write(indata)
#0 
#0 #print "Alright, all done."
#0 
#0 out_file.close()
#0 in_file.close()

#1 THIS IS THE SHORTER CODE THAN ZED'S ONE,BY STACKOVERFLOW:
from sys import argv; open(argv[2], 'w').write(open(argv[1]).read())
# ";" combines 2 lines to one :))
# open my ex17phuong.py by notepad++ for more details :)))))))




