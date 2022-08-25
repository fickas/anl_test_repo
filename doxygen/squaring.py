def square(x=10:int) -> int:
  """!
  @brief Squares an integer.

  @details Squares an integer by multiplication.
  Might be faster than ^ operator.

  @author Stephen Fickas

  @callgraph
  @callergraph

  @param x [=10:int]   Number to square. Optional value = 10.

  @return [int] Squared value of input.
  """
  return x*x

def square_square(x=100:int):
  """!
  @brief Squares the square of input.

  @details Squares the square by using the square function.
  Might be slower than ^ operator.

  @author Stephen Fickas

  @callgraph
  @callergraph

  @param x [=100:int]   Number to square square. Optional value = 100.

  @return [int] Squared square value of input.
  """
  
  return square(square(x))
