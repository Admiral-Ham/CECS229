from Vec import Vec
import math
"""-------------------- PROBLEM 1 --------------------"""
class Matrix:
 
    def __init__(self, rows):
        """
        initializes a Matrix with given rows
        :param rows: the list of rows that this Matrix object has
        """
        self.rows = rows
        self.cols = []
        self._construct_cols()
        return
 
    """
  INSERT MISSING SETTERS AND GETTERS HERE
  """
    #Setters
    def set_row(self, i, new_row):
        if len(self.rows[i - 1]) != len(new_row):
            raise ValueError("Incompatible row length.")
 
        for j in range(len(self.rows[0])):
            self.rows[i - 1][j] = new_row[j]
        self._construct_cols()
        
    def set_col(self, j, new_cols):
        if len(self.cols[j - 1]) != len(new_cols):
            raise ValueError("Incompatible column length.")
        
        for i in range(len(self.cols[0])):
            self.cols[j - 1][i] = new_cols[i]
        self._construct_rows()
        
 
    def set_entry(self, i, j, val):
        if i <= 0 or i >= len(self.rows) + 1:
            raise IndexError("Incompatible row.")
        if j <= 0 or j >= len(self.cols) + 1:
            raise IndexError("Incompatible column.")
        self.rows[i - 1][j - 1] = val
        self._construct_cols()
        return
    
    #Getters
    def get_row(self, i):
        if i <= 0 or i >= len(self.rows) + 1:
            raise IndexError(f"There is no row at index {i}")
        return self.rows[i - 1]
    
    def get_col(self, j):
        if j <= 0 or j >= len(self.cols) + 1:
            raise IndexError(f"There is no column at index {j}")
        return self.cols[j - 1]
    
    def get_entry(self, i, j):
        if i <= 0 or i >= len(self.rows) + 1:
            raise IndexError("Incompatible row.")
        if j <= 0 or j >= len(self.cols) + 1:
            raise IndexError("Incompatible column.")
        return self.rows[i - 1][j - 1]
    
    def get_columns(self):
      cols = []
      for i in range(len(self.cols)):
        cols.append([])
        for j in range(len(self.cols[0])):
          cols[i].append(self.cols[i][j])
      return cols

    
    def get_rows(self):
        rows = []
        for i in range(len(self.rows)):
            rows.append([])
            for j in range(len(self.rows[0])):
                rows[i].append(self.rows[i][j])
        return rows
    
    def get_diag(self, k):
        diag = []
        if k > 0:
            for i in range(len(self.rows)):
                if k >= len(self.rows):
                    break
                diag.append(self.rows[i][k])
                k += 1
        else:
            for i in range(len(self.rows)):
                if (i - k) >= len(self.rows) or i >= len(self.cols):
                    break
                diag.append(self.rows[i - k][i])
        
        return diag
 
            
 
    def _construct_cols(self):
        """
        HELPER METHOD: Resets the columns according to the existing rows
        """
        self.cols = []
        # FIXME: INSERT YOUR IMPLEMENTATION HERE
        num_cols = len(self.rows[0])
        for i in range(num_cols):
            self.cols.append([])
            for j in range(len(self.rows)):
                self.cols[i].append(self.rows[j][i])
        return
 
    def _construct_rows(self):
        """
        HELPER METHOD: Resets the rows according to the existing columns
        """
        self.rows = []
        # FIXME: INSERT YOUR IMPLEMENTATION HERE
        num_rows = len(self.cols[0])
        for i in range(num_rows):
            self.rows.append([])
            for j in range(len(self.cols)):
                self.rows[i].append(self.cols[j][i])
        return
 
    def __add__(self, other):
        """
        overloads the + operator to support Matrix + Matrix
        :param other: the other Matrix object
        :raises: ValueError if the Matrix objects have mismatching dimensions
        :raises: TypeError if other is not of Matrix type
        :return: Matrix type; the Matrix object resulting from the Matrix + Matrix operation
        """
        # FIXME: REPLACE WITH IMPLEMENTATION
        if type(other) != Matrix:
            raise TypeError("The other object is not a matrix.")
        if len(self.rows) != len(other.rows) or len(self.cols) != len(other.cols):
            raise ValueError("Matrix objects do not have the same dimensions.")
            
        temp_matrix = Matrix(self.get_rows())
        for i in range(1 ,len(self.rows) + 1):
          for j in range(1, len(self.rows[0]) + 1):
            val = self.get_entry(i, j) + other.get_entry(i, j)
            temp_matrix.set_entry(i, j, val)
 
        return temp_matrix
    def __sub__(self, other):
        """
        overloads the - operator to support Matrix - Matrix
        :param other:
        :raises: ValueError if the Matrix objects have mismatching dimensions
        :raises: TypeError if other is not of Matrix type
        :return: Matrix type; the Matrix object resulting from Matrix - Matrix operation
        """
        # FIXME: REPLACE WITH IMPLEMENTATION
        if type(other) != Matrix:
            raise TypeError("The other object is not a matrix.")
        if len(self.rows) != len(other.rows) or len(self.cols) != len(other.cols):
            raise ValueError("Matrix objects do not have the same dimensions.")
 
        temp_matrix = Matrix(self.get_rows())
        for i in range(1 ,len(self.rows) + 1):
          for j in range(1, len(self.rows[0]) + 1):
            val = self.get_entry(i, j) - other.get_entry(i, j)
            temp_matrix.set_entry(i, j, val)
        return temp_matrix
 
    def __mul__(self, other):
        """
        overloads the * operator to support
            - Matrix * Matrix
            - Matrix * Vec
            - Matrix * float
            - Matrix * int
        :param other: the other Matrix object
        :raises: ValueError if the Matrix objects have mismatching dimensions
        :raises: TypeError if other is not of Matrix type
        :return: Matrix type; the Matrix object resulting from the Matrix + Matrix operation
        """
        val_list = []
        if type(other) == float or type(other) == int:
            temp_matrix = Matrix(self.get_rows())
            for i in range(1 ,len(self.rows) + 1):
                for j in range(1, len(self.rows[0]) + 1):
                    val = self.get_entry(i, j) * other
                    temp_matrix.set_entry(i, j, val)
            return temp_matrix
 
        elif type(other) == Matrix:
            if len(self.cols) != len(other.rows):
                raise ValueError("Matrix obejects have the mismatching dimensions.")
            
            
            for i in range(len(self.rows)):
              listc = self.get_row(i+1)
              listb = []
              for j in range(len(other.cols)):
                temp0 = other.get_col(j+1)
                temp = [listc[k]*temp0[k] for k in range(len(listc))]
                sums = sum(temp)
                listb.append(sums)
              val_list.append(listb)
            return Matrix(val_list)
 
        elif type(other) == Vec:
            if len(self.cols) != len(other):
              raise  ValueError("Matrix or Vector have the mismatching dimensions.")
            product = 0
            for i in range(len(self.rows)):
                product = 0
                for j in range(len(self.cols)):
                    product += self.get_entry(i+1, j+1) * other[j]
                val_list.append(product)
            return(Vec(val_list))
        else:
            raise TypeError(f"Matrix * {type(other)} is not supported.")
        return
 
    def __rmul__(self, other):
        """
        overloads the * operator to support
            - float * Matrix
            - int * Matrix
        :param other: the other Matrix object
        :raises: ValueError if the Matrix objects have mismatching dimensions
        :raises: TypeError if other is not of Matrix type
        :return: Matrix type; the Matrix object resulting from the Matrix + Matrix operation
        """
        if type(other) == float or type(other) == int:
            temp_matrix = Matrix(self.get_rows())
            for i in range(1 ,len(self.rows) + 1):
                for j in range(1, len(self.rows[0]) + 1):
                    val = self.get_entry(i, j) *other
                    temp_matrix.set_entry(i, j, val)
            return temp_matrix
        else:
            raise TypeError(f"{type(other)} * Matrix is not supported.")
        return
 
    '''-------- ALL METHODS BELOW THIS LINE ARE FULLY IMPLEMENTED -------'''
 
    def dim(self):
        """
        gets the dimensions of the mxn matrix
        where m = number of rows, n = number of columns
        :return: tuple type; (m, n)
        """
        m = len(self.rows)
        n = len(self.cols)
        return (m, n)
 
    def __str__(self):
        """prints the rows and columns in matrix form """
        mat_str = ""
        for row in self.rows:
            mat_str += str(row) + "\n"
        return mat_str
 
    def __eq__(self, other):
        """
        overloads the == operator to return True if
        two Matrix objects have the same row space and column space
        """
        if type(other) != Matrix:
            return False
        this_rows = [round(x, 3) for x in self.rows]
        other_rows = [round(x, 3) for x in other.rows]
        this_cols = [round(x, 3) for x in self.cols]
        other_cols = [round(x, 3) for x in other.cols]
 
        return this_rows == other_rows and this_cols == other_cols
 
    def __req__(self, other):
        """
        overloads the == operator to return True if
        two Matrix objects have the same row space and column space
        """
        if type(other) != Matrix:
            return False
        this_rows = [round(x, 3) for x in self.rows]
        other_rows = [round(x, 3) for x in other.rows]
        this_cols = [round(x, 3) for x in self.cols]
        other_cols = [round(x, 3) for x in other.cols]
 
        return this_rows == other_rows and this_cols == other_cols
 
 
"""-------------------- PROBLEM 2 --------------------"""
 
 
def rotate_2Dvec(v: Vec, tau: float):
    """
    computes the 2D-vector that results from rotating the given vector
    by the given number of radians
    :param v: Vec type; the vector to rotate
    :param tau: float type; the radians to rotate by
    :return: Vec type; the rotated vector
    """
    if len(v) != 2:
        raise ValueError("Vector must be 2D.")

    x, y = v[0], v[1]
    new_x = x * math.cos(tau) - y * math.sin(tau)
    new_y = x * math.sin(tau) + y * math.cos(tau)
    return Vec([new_x, new_y])