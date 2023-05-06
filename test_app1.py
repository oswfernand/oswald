from app1 import add,sub,divide,multiply

def test_add():
    assert add(2,3) == 5

def test_sub():
    assert sub(2,1) == 1
    
def test_divide():
    assert divide(4,2) == 2
    
def test_multiply():
    assert multiply(2,3) == 6