from arithmetic import sub

  def test_sub():
    assert sub(2,1)==1
    assert sub(.3333, .1111)==.2222
    assert sub(.3333, .1111, round=2)==.22
    
