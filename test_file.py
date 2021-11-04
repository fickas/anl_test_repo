#print hello name!
def hello(name='Steve'):
  return f'Hello {name}!'

def test_hello():
  name = 'Steve'
  assert hello()==f'Hello {name}!'
