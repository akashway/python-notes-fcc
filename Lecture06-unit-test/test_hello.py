from hello import hello

'''
def test_hello():
    assert hello("Vikash")=="Hello, Vikash"

'''

'''
run cmd:
pytest .\test_hello.py  

Output:
test_hello.py .                                                                                                                       [100%] 

============================================================ 1 passed in 0.02s =============================================================
'''


def test_default():
    assert hello()=="Hello, World"

def test_argument():
    assert hello("Jhon")=="Hello, Jhon"

'''
run cmd:
pytest .\test_hello.py  

output:
test_hello.py ..                                                                                                                      [100%] 

============================================================ 2 passed in 0.02s ============================================================= 
'''