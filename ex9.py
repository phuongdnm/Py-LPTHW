# Here's some new strange stuff, remember type it exactly

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days
print "Here are the months: ", months

print """ 
There's somthing going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
ok line 5
now is the line 6
and line 7
...
now is the line 10000 :)) 
now is the line 10000000 :)) 
"""
# after """,you can write as many as you can :))
print "%s" %"\n" *5 

#common student questions 2: Why do the \n newlines not work when I use %r?
print "Minh %r Phuong" % "\n"
print "Minh %s Phuong" % "\n"
