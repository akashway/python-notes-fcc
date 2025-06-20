def main():
    x=int(input("What's x? "))
    print("x square is",square(x))

def square(x):
    # return x*x
    return x+x

if __name__=="__main__":
    main()

'''
__main__
When you run a script directly, __name__ == "__main__".
When you import that same script as a module, __name__ becomes the module's name.
Helps prevent certain code from running during imports (commonly used to guard the main() function).
'''