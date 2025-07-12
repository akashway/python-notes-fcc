import argparse
import sys


'''
# Version 1
if len(sys.argv)==1:
    print("meow!")

elif len(sys.argv)==3 and sys.argv[1]=="-n":
    n=int(sys.argv[2])
    for _ in range(n):
        print("meow!")

else:
    print("usage: meows.py")

'''

r'''
output:
python .\meows-arg.py     
meow!

python .\meows-arg.py 3   
usage: meows.py

python .\meows-arg.py -n 3
meow!
meow!
meow!
'''

'''
# Version 2
parser=argparse.ArgumentParser()
parser.add_argument("-n")
args=parser.parse_args()

for _ in range(int(args.n)):
    print("meow!")
'''

r'''
output:
python meows-arg.py -n 3
meow!
meow!
meow!

python meows-arg.py
  File "C:\Users\akash\Akash'sTask\Python\python-fcc\Lecture10-misc\meows-arg.py", line 37, in <module>
    for _ in range(int(args.n)):
                   ~~~^^^^^^^^
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'NoneType'


python meows-arg.py -h
usage: meows-arg.py [-h] [-n N]

options:
  -h, --help  show this help message and exit
  -n N
'''


'''
# Version 3
parser=argparse.ArgumentParser(description="meow like a cat")
parser.add_argument("-n",help="number of time to meow")
args=parser.parse_args()

for _ in range(int(args.n)):
    print("meow!")
'''

'''
Output:
python meows-arg.py -h
usage: meows-arg.py [-h] [-n N]

meow like a cat

options:
  -h, --help  show this help message and exit
  -n N        number of time to meow
'''


#Version 4
parser=argparse.ArgumentParser(description="meow like a cat")
parser.add_argument("-n",default=1,help="number of time to meow",type=int)
args=parser.parse_args()

for _ in range(args.n):
    print("meow!")


'''
Since we added type=int inside add_argument we don't have to convert into int now

output:
python meows-arg.py
meow!

now not getting error beacuse we provided a default value
'''