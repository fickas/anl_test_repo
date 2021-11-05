## @package anl_test_repo
#  Attempting to mock portions of Flash project.

##add function
#Adds two numbers.
#  @param x a number.
#  @param y a number.
def add(x,y):
  return x+y

##sub function
#Subtracts two numbers.
#  @param x a number.
#  @param y a number.
def sub(x,y):
  return x-y

##list_add function
#Adds two lists of numbers.
#  @param list1 a list of numbers.
#  @param list2 a list of numbers.
def list_add(list1, list2):
  assert len(list1)==len(list2)
  new_list = [add(x,y) for x,y in zip(list1, list2)]
  return new_list
