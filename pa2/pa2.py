import math
""" ----------------- PROBLEM 1 ----------------- """


def primes(a, b):
  """
      prints all primes in the range [a, b]
      :@param a: int type; a positive integer greater than 1
      :@param b: int type; a positive integer greater than or equal to a.
      :@return: set type; a set of all primes in the range [a, b]
      :@raises ValueError if a < 1 or b < a
      """
  if a < 1 or b < a:  # handling invalid range
    raise ValueError("Invalid range given")

  if a == 1:  # handling starting point a = 1
    a = 2  # this ensures 1 is not listed as a prime

  # FIXME: initialize `stop` which is the stopping criteria for
  #        the loop in the Sieve of Eratosthenes
  stop = math.floor(math.sqrt(b))

  # FIXME: initialize a Python set called `P` that contains
  #        all integers in the range [a, b]
  P = set(x for x in range(a, b + 1))

  for x in range(2, stop + 1 ):

    # FIXME: use Python list comprehension to create a set
    #        of multiples of x in the range [2, b];
    # HINT: the set of multiples of x can be expressed as
    #       k * x, where k is an integer; hence the comprehension
    #       should loop over values that satisfy k * x <= b
    #print(x)
    multiples_x = set(n for n in P if (n % x == 0) and (n // x != 1) )
    
    P -= multiples_x  # removing the multiples of x from the set P

  return P


""" ----------------- PROBLEM 2 ----------------- """


def bezout_coeffs(a, b):
  """
      computes the Bezout coefficients of two given positive integers
      :param a: int type; positive integer
      :param b: int type; positive integer
      :returns: dict type; a dictionary with parameters a and b as keys,
                and their corresponding Bezout coefficients as values.
      :raises: ValueError if a < 0 or b < 0
      """
  if a < 0 or b < 0:
    raise ValueError(
      f"bezout_coeffs(a, b) does not support negative arguments.")
  s0 = 1
  t0 = 0
  s1 = -1 * (b // a)
  t1 = 1

  temp = b
  bk = a
  ak = temp % a

  while ak != 0:
    temp_s = s1
    temp_t = t1

    # FIXME: Update s1 according to the formula for sk
    s1 = s0 - s1 * (bk // ak)

    # FIXME: Update t1 according to the formula for tk
    t1 = t0 - t1 * (bk // ak)

    s0 = temp_s
    t0 = temp_t
    temp = bk

    # FIXME: Update bk and ak
    bk = ak
    ak = temp % ak

  # FIXME: Replace each string with the correct coefficients of a and b
  return {a: s0, b: t0}


""" ----------------- PROBLEM 3 ----------------- """


def gcd(a, b):
  
  """
    computes the greatest common divisor of two given integers
    :param a: int type;
    :param b: int type;
    :returns: int type; the gcd of a and b
    """
  A = abs(a)
  B = abs(b)
  if A == B:
    return A  # FIXME: replace this pass with the correct return value
  bez = bezout_coeffs(A, B)
  return  (A * bez[A] + B * bez[B] )# FIXME: replace this pass with the correct return value


""" ----------------- PROBLEM 4 ----------------- """


def mod_inv(a, m):
  """
    computes the inverse of a given integer a under a given modulo m
    :param a: int type; the integer of interest
    :param m: int type; the modulo
    :returns: int type; the integer in range [0, m) that is the inverse of a under modulo m
    :raises: ValueError if m < 0 or if a and m are not relatively prime
    """
  if m < 0:
    raise ValueError(f"mod_inv(a, m) does not support negative modulo m = {m}")
  g = gcd(a, m)
  if g != 1:
    raise ValueError(
      f"mod_inv(a, m) does not support integers that are not relatively prime.\nGCD of {a} and {m} is {g}."
    )
  A = a
  while A < 0:

    A += m #"""FIXME: replace this string so that by the end of the loop, A is in range [0, m) and is equivalent to a under modulo m"""

  inverse = bezout_coeffs(A, m)[A] #"""FIXME: replace this string with the inverse of a under modulo m"""

  while inverse < 0:

    inverse += m #"""FIXME: replace this string so that by the end of the loop, the inverse is in range [0, m)"""

  return inverse


""" ----------------- PROBLEM 5 ----------------- """


def solve_mod_equiv(a, b, m, low, high):
  pass
  """
    computes all solutions to the equivalence ax ≡ b (mod m)
    that are in the range [low, high]
    :param a: int type; the coefficient of the unknown value x
    :param b: int type; the integer that ax is equivalent to
              under modulo m
    :param m: int type; the modulo
    :param low: int type; the lower bound for the solutions
    :param high: int type; the upper bound for the solutions
    :raises: ValueError if high < low or if m < 0
    """
  if high < low:
    raise ValueError(
      f"solve_mod_equiv() does not support the upper bound {high} less than the lower bound {low}"
    )
  if m < 0:
    raise ValueError(
      f"solve_mod_equiv() does not support negative modulo m = {m}")
  
  g = gcd(a, m)
  if g != 1:
    raise ValueError(
      f"mod_inv(a, m) does not support integers that are not relatively prime.\nGCD of {a} and {m} is {g}."
    )
  
  a_inv = mod_inv(a, m)

  k_low = math.ceil((low - a_inv * b) / m) #"""FIXME: replace this string with the correct lower bound for k, if x = mk + a_inv * b is a solution in the range [low, high]"""

  k_high = math.floor((high - a_inv * b) / m) #"""FIXME: replace this string with the correct upper bound for k, if x = mk + a_inv * b is a solution in the range [low, high]"""

  x = ((n * m + a_inv * b) for n in range(k_low, k_high + 1))  
  #"""FIXME: replace this string with the Python list comprehension that uses x = mk + a_inv * b to generate all solutions to ax ~ b (mod m) in the range [low, high]"""
  return set(x)
