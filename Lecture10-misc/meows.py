def meow(n:int):
    for _ in range(n):
        print("meow")


meow(3)

# lets run by mypy meows.py

# mypy meows.py
# Success: no issues found in 1 source file


# let's try with str
meow("akash")
'''
mypy meows.py
meows.py:15: error: Argument 1 to "meow" has incompatible type "str"; expected "int"  [arg-type]
Found 1 error in 1 file (checked 1 source file)
'''


def meow2(n:int):
    for _ in range(3):
        print("meow")


n:int=input("Number? ")

meow2(n)

'''
mypy meows.py
meows.py:15: error: Argument 1 to "meow" has incompatible type "str"; expected "int"
  [arg-type]
meows.py:28: error: Incompatible types in assignment (expression has type "str", variable has type "int")  [assignment]
Found 2 errors in 1 file (checked 1 source file)
'''


def meow3(n:int):
    print("meow")

n1:int=int(input("Enter another number? "))

meows:str=meow3(n1)
print(meows)

'''
output:
meow
meow
meow
None

three meows why?
because in function we are printing
but
Why output is None?
beacuse function does not written anything
so if something is there which checks whether function returning specified data type
then it is good we can catch error earl

'''

def meow4(n:int)->str:
    return "meow\n"*n

n2:int=int(input("Enter n2? "))


meows2:str=meow3(n2)
print(meows2,end="")

'''
Now mypy will not give any error
'''