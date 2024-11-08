import math

""" ----------------- PROBLEM 1 ----------------- """
def translate(S, z0):
  """
  translates the complex numbers of set S by z0
  :param S: set type; a set of complex numbers
  :param z0: complex type; a complex number
  :return: set type; a set consisting of points in S translated by z0
  """
  set_t = set()
  for x in S:
     set_t.add(x + z0)
  # FIXME: Implement this function
  # FIXME: Return correct output
  return set_t


""" ----------------- PROBLEM 2 ----------------- """
def scale(S, k):
  """
  scales the complex numbers of set S by k.  
  :param S: set type; a set of complex numbers
  :param k: float type; positive real number
  :return: set type; a set consisting of points in S scaled by k
  :raise: raises ValueError if k <= 0       
  """
  if k <= 0:
     raise ValueError("K is negative")
  scale_set = set()
  for x in S:
     scale_set.add(x * k)
  # FIXME: Implement this function.
  # FIXME: Return correct output
  return scale_set


""" ----------------- PROBLEM 3 ----------------- """
def rotate(S, tau):
    """
    rotates the complex numbers of set S by tau radians.  
    :param S: set type; - set of complex numbers
    :param tau: float type; radian measure of the rotation value. 
                If negative, the rotation is clockwise.  
                If positive the rotation is counterclockwise. 
                If zero, no rotation.
    :returns: set type; a set consisting of points in S rotated by tau radians
    """
    r_set = set()
    c_tau = math.cos(tau)
    s_tau = math.sin(tau)
    for x in S:
        r_set.add(complex(x.real * c_tau - x.imag * s_tau, x.real * s_tau + x.imag * c_tau))
    # FIXME: Implement this function. 
    # FIXME: Return correct output
    return r_set


""" ----------------- PROBLEM 4 ----------------- """
class Vec:
  def __init__(self, contents = []):
      """
      Constructor defaults to empty vector
      INPUT: list of elements to initialize a vector object, defaults to empty list
      """
      self.elements = contents
      return

  def __abs__(self):
      """
      Overloads the built-in function abs(v)
      :returns: float type; the Euclidean norm of vector v
      """
      mag = 0
      for i in self.elements:
         mag += i ** 2
      # FIXME: Implement this method
      # FIXME: Return correct output
      return math.sqrt(mag)

  def __add__(self, other):
      """
      overloads the + operator to support Vec + Vec
      :raises: ValueError if vectors are not same length 
      :returns: Vec type; a Vec object that is the sum vector of this Vec and 'other' Vec
      """
      if len(self.elements) != len(other.elements):
          raise ValueError ("Vectors are not the same size.")
      sum = []
      for i in range(len(self.elements)):
          sum.append(self.elements[i] + other.elements[i])
      # FIXME: Finish the implementation
      # FIXME: Return correct output
      return Vec(sum) 

  def __sub__(self, other):
      """
      overloads the - operator to support Vec - Vec
      :raises: ValueError if vectors are not same length 
      :returns: Vec type; a Vec object that is the difference vector of this Vec and 'other' Vec
      """
      if len(self.elements) != len(other.elements):
          raise ValueError ("Vectors are not the same size.")
      sub = []
      for i in range(len(self.elements)):
          sub.append(self.elements[i] - other.elements[i])
      # FIXME: Finish the implementation
      # FIXME: Return correct output
      return Vec(sub)



  def __mul__(self, other):
      """
      Overloads the * operator to support 
          - Vec * Vec (dot product) raises ValueError if vectors are not 
            same length in the case of dot product; returns scalar
          - Vec * float (component-wise product); returns Vec object
          - Vec * int (component-wise product); returns Vec object

      """
      if type(other) == Vec: #define dot product
          if len(self.elements) != len(other.elements):
            raise ValueError ("Vectors are not the same size.")
          dot_product = 0
          for i in range(len(self.elements)):
             dot_product += self.elements[i] * other.elements[i]
          # FIXME: Complete the implementation
          # FIXME: Return the correct output
          return dot_product

      elif type(other) == float or type(other) == int: #scalar-vector multiplication
        list = []
        for i in range(len(self.elements)):
            list.append(self.elements[i] * other)
        return Vec(list)


  def __rmul__(self, other):
      """
      Overloads the * operation to support 
          - float * Vec; returns Vec object
          - int * Vec; returns Vec object
      """
      list = []
      for i in range(len(self.elements)):
        list.append(self.elements[i] * other)
      # FIXME: Complete the implementation
      # FIXME: Return the correct output
      return Vec(list)



  def __str__(self):
      """returns string representation of this Vec object"""
      return str(self.elements) # does NOT need further implementation