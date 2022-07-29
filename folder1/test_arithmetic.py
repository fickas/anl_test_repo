from arithmetic import sub

#Unit tests for sub function
def test_sub():
  assert sub(2,1)==1
  assert sub(4,2)==2
  assert sub(.3333, .1111, round=4)==.2222
  assert sub(.3333, .1111, round=2)==.22
    
