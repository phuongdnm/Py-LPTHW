from sys import argv 

script, first, second, third = argv 
#goi ra 4 bien trong hang trieu bien cua thu vien argv,de cho chuong trinh nhe

print "The script is called: " , script #mac dinh no se hien ra ten file
print "Your first varialbe is: ", first #hien ra bien thu nhat sau tu python .\ex13.py
print "Your second variable is: ", second #tuong tu tren
print "Your third variable is: ", third

#loi hay mac phai: luc compile bang powershell,no bao loi:

#"Traceback (most recent call last):
#  File ".\ex13.py", line 3, in <module>
#    script, first, second, third = argv
#ValueError: need more than 1 value to unpack"

#phai compile bang lenh: python .\ex13.py dinh nhu minh

#study drill 3: toi da viet o file ex13sd.py
