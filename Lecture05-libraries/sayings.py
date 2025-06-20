def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

# main() 
# if we write like this then even we import the file in another file it will run all the function

# write like this


print(__name__) 
'''
If we run the current script then 
__name__ will print __main__
if we import this file in another script then
__name__ will print name of that script
'''

if __name__=="__main__":
    main()
