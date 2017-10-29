#i = 0
#numbers = []

#while i < 10: 
#    print "At the top i is %d" % i
#    numbers.append(i)
#
#    i = i + 2
#    print "Number now: ", numbers
#    print "At the bottom i is %d" % i

#print "The numbers: "

#for num in numbers:
#    print num

### STUDY DRILL 1: Convert this while-loop to a function
def while_loop(x,a):
    i = 10
    numbers = []
    while i > x :
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + a
        print "Number now: ", numbers
        print "At the bottom i is %d" %i

def for_loop(u,v):
    elements = []
    for i in range(0,u,v): 
        elements.append(i)
    
    print elements

x = int(raw_input('while-loop top: '))
a = int(raw_input('while-loop step: '))
while_loop(x,a)
print "\n"


u = int(raw_input("for-loop top: "))
v = int(raw_input("for-loop step: "))
for_loop(u,v) 

### Let's try with i = 10 and i > x :)))))



