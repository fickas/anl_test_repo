
#Adding this comment to just test committing and diff data
def sub(x,y):
  """
  Return the subtraction of two numbers::

  .. math:: `\mathtt{x} - \mathtt{y}'

  Parameters
  ----------
  x: int, real, complex
     first operand
  y: int, real, complex
     second operand
  round: positive int, optional
     If None, does no rounding. Else rounds the result to places specified, e.g., 2.

  Returns
  -------
  z: int, real, complex
      the result of subtraction

  Raises
  ------
  ValueError:
      when 'x' or 'y' is not a number

  See Also
  --------
  Of course, subtraction is built-in to Python as minus sign.

  Notes
  -----
  The algorithm is a straightforward implementation of
  subtraction.

  References
  ----------
  .. [1] Any textbook on mathematics.

  Examples
  --------
  >>> sub(1,2)
  -1
  >>> sub(.03333, .01111)
  .02222
  >>> sub(.03333, .01111, round=3)
  .022
  """
  return x-y

def list_sub(list1, list2):
  assert len(list1)==len(list2)
  new_list = [sub(x,y) for x,y in zip(list1, list2)]
  return new_list

#Adding this comment to just test committing and diff data
def prod(A):
  """
  Return the product of all numbers within a list of numbers::

  .. math:: `\prod_{a \in A} a'

  Parameters
  ----------
  A: list of numbers

  Returns
  -------
  product: product of all numbers in A. If A is empty, return 1.

  Raises
  ------
  TypeError:
      when an element of A does not support multiplication

  See Also
  --------
  prod function from numpy library

  Notes
  -----
  This is algorithm is linear in the length of A.

  References
  ----------
  .. [1] Any textbook on mathematics.

  Examples
  --------
  >>> prod([1,2,0])
  0
  >>> prod([.03333, .01111])
  0.0003702963
  >>> prod([])
  1
  """
  
  product = 1
  for a in A:
    product *= a

  return product
    