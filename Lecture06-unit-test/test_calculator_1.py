from calculator import square


def main():
    # test_square_1()
    # test_square_2()
    test_square_3()

'''
def test_square_1():
    if square(2)!=4:
        print("2 squared was not 4")
    if square(3)!=9:
        print("3 squared was not 9")
'''

'''
output:
3 squared was not 9
'''

'''
why moved to next approach?
to just two lines of code we are writing 4 lines of code
'''


'''
def test_square_2():
    assert square(2)==4
    assert square(3)==9

'''

'''
output:

assert square(3)==9
AssertionError

like we try to solve the no. of lines of code but the
error we error getting is to difficult to understand and lets try
to refactor using try-except
'''


def test_square_3():
    try:
        assert square(2)==4
    except AssertionError:
        print("2 square is not 4")
    try:
        assert square(3)==9
    except AssertionError:
        print("3 square is not 9")
    try:
        assert square(-2)==4
    except AssertionError:
        print("-2 square is not 4")
    try:
        assert square(-3)==9
    except AssertionError:
        print("-3 square is not 9")
    try:
        assert square(0)==0
    except AssertionError:
        print("0 square is not 0")



'''
Output:
3 square is not 9
-2 square is not 4
-3 square is not 9

so again we came to that issue again so many lines of code
to just test a one line of code
'''

'''
here come to rescue us testing library
we are using pytest (3rd party library)
it will handle try except its own i have to just write assert
will see demo in another file
'''
if __name__=="__main__":
    main()