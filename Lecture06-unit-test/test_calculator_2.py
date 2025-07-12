from calculator import square
import pytest
'''
so we have created a file with a single function
how we will run?
erlier we have running files like python file.py
now we have to write
pytest file.py (pytest .\test_calculator_2.py)
and in this files all the function will run
'''

'''
def test_square():
    assert square(2)==4
    assert square(-2)==4
    assert square(3)==9
    assert square(-3)==9
    assert square(0)==0
'''

'''
run cmd:
pytest .\test_calculator_2.py

Output:
test_calculator_2.py F

    def test_square():
        assert square(2)==4
>       assert square(-2)==4
E       assert -4 == 4
E        +  where -4 = square(-2)
'''

'''
see the above output
as soon as the test failed next all assert statement did not run
hence it is good to create multiple function to test a function
'''

def test_positive():
    assert square(2)==4
    assert square(3)==9

def test_negative():
    assert square(-2)==4
    assert square(-3)==9

def test_zero():
    assert square(0)==0

def test_str():
    with pytest.raises(TypeError):
        square("cat")

'''
Run the code inside this block (square("cat")) — and 
expect that it will raise a TypeError. 
If it does, the test passes. If it doesn't raise a TypeError, 
the test fails.”

"Expect a TypeError to be raised when calling square('cat')."

“While I'm inside this with block, I expect this specific thing (a TypeError) to happen.”

since my 
def square(x):
    # return x*x
    return x+x

does not raise TypeError hence the test will failed
if we want to pass that test:

def square(x):
    if not isinstance(x,int):
        raise TypeError("Must be int")
    return x*x
'''

'''
run cmd:
pytest .\test_calculator_2.py

Output:
test_calculator_2.py FF.     
def test_positive():
        assert square(2)==4
>       assert square(3)==9
E       assert 6 == 9
E        +  where 6 = square(3)

test_calculator_2.py:40: AssertionError
______________________________ test_negative ______________________________ 

    def test_negative():
>       assert square(-2)==4
E       assert -4 == 4
E        +  where -4 = square(-2)

test_calculator_2.py:43: AssertionError
'''
