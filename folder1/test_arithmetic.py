from arithmetic import sub, prod

#Adding this comment to just test committing and diff data
def test_sub():
  assert sub(2,1)==1
  assert sub(4,2)==2
  assert sub(.3333, .1111)==.2222
  assert sub(.3333, .1111, round=2)==.22

def test_prod():
  assert prod([])==1
  assert prod([1,2,0])==0
  assert prod([.03333, .01111]) - 0.0003702963 < 1e-10
    
