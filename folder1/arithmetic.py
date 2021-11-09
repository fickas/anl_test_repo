

def sub(x,y,round=None):
      """
    Return a list of random ingredients as strings.

    :param kind: Optional "kind" of ingredients.
    :type kind: list[str] or None
    :raise lumache.InvalidKindError: If the kind is invalid.
    :return: The ingredients list.
    :rtype: list[str]

    """
  """
  Return the subtraction of two numbers::

  .. math:: x - y = z

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
  >>> sum(.03333, .01111)
  .02222
  >>> sum(.03333, .01111, round=3)
  .022
  """
  return x-y

##list_sub function
#subss two lists of numbers.
#  @param list1 a list of numbers.
#  @param list2 a list of numbers.
def list_sub(list1, list2):
  assert len(list1)==len(list2)
  new_list = [sub(x,y) for x,y in zip(list1, list2)]
  return new_list
