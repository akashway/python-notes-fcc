from hello import hello

def test_default():
    assert hello()=="Hello, World"

def test_argument():
    assert hello("Jhon")=="Hello, Jhon"

'''
Running whole pacakge but geeting import error
so i moved hello.py itself inside the test-package
'''