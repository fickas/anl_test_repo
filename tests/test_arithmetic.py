
from arithmetic import sub

#Adding this comment to just test committing and diff data
def test_sub():
  assert sub(2,1)==1
  assert sub(4,2)==2
  assert sub(6,2)==4
  assert sub(.3333, .1111, round=4)==.2222
  assert sub(.3333, .1111, round=2)==.22
