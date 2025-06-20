# Usually when we take a input from user it will prompt a msg
# for a user to give an Input but we can take intput while writing
# a command to run python file 
# like we write python name.py so just after writing this
# we can provide the input which is nedded in program we use sys module

import sys

'''
print("hello, file name which we running", sys.argv[0])
print("hello, my name is", sys.argv[1])
'''

'''
when i am giving this cmd: python name.py AkashMishra
output:
hello, file name which we running name.py
hello, my name is AkashMishra
'''

'''
when i am giving cmd : python name.py
output:
hello, file name which we running name.py
Error:
print("hello, my name is", sys.argv[1])
IndexError: list index out of range
'''

'''
try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Please provide a name")
'''

'''
if len(sys.argv)<2:
    print("Too few arguments")
elif len(sys.argv)>2:
    print("Too many arguments")
else:
    print("hello, my name is",sys.argv[1])

'''


'''
cmd:python name.py "Akash Mishra"

output:
hello, my name is Akash Mishra
'''


#some approach where seprate the logic and error part but if we run like
# this we will get error think what error coul be
'''
if len(sys.argv)<2:
    print("Too few arguments")
elif len(sys.argv)>2:
    print("Too many arguments")

print("hello, my name is",sys.argv[1])
'''

'''
if len(sys.argv)<2:
    sys.exit("Too few arguments")
elif len(sys.argv)>2:
    sys.exit("Too many arguments")

print("hello, my name is",sys.argv[1])
'''

'''
if len(sys.argv)<2:
    sys.exit("too few arguments")

for arg in sys.argv:
    print(arg)

'''

'''
cmd: python name.py a b c

output:
name.py
a
b
c
'''


if len(sys.argv)<2:
    sys.exit("too few arguments")

for arg in sys.argv[1:]:
    print(arg)

'''
cmd: python name.py a b c

output:
a
b
c
'''