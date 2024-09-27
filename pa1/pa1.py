import math
""" ---------------- PROBLEM 1 ----------------"""


def equiv_to(a, m, low, high):
    k_low = math.ceil((low - a) / m) # wrong; replace 'low' with the correct value
    k_high = math.floor((high - a)/ m)  # wrong; replace 'high' the correct value
    k_vals = list(range(k_low, k_high + 1))
    x_vals = [a + m * k for k in k_vals ]  
    return x_vals


""" ---------------- PROBLEM 2 ----------------"""


def b_rep(n, b):
    pass
    digits = []  # stores the digits of the b-representation of n
    digits_str =""
    q = n
    while q != 0:
        digit = q % b #fixme: update 'digit' to be the remainder of q divided by b"
        if b == 16 and digit > 9:
            hex_dict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
            digit = hex_dict[digit] # fixme: Update digit = ...
        digits.append(digit)
        q = q // b   #"FIXME: update q to the correct value."
    digits.reverse()
    for i in range(len(digits)):
        digits_str += str(digits[i])
    return digits_str # FIXME: Return the string of digits


""" ---------------- PROBLEM 3 ----------------"""


def binary_add(a, b):
    pass
    # removing all whitespace from the strings
    a = a.replace(' ', '')
    b = b.replace(' ', '')

    # padding the strings with 0's so they are the same length
    if len(a) < len(b):
        diff = len(b) - len(a)
        a = "0" * diff + a
    elif len(a) > len(b):
        diff = len(a) - len(b)
        b = "0" * diff + b

    # addition algorithm
    result = ""
    carry = 0
    for i in reversed(range(len(a))):
        a_i = int(a[i])
        b_i = int(b[i])

        result = str((a_i + b_i + carry) % 2 ) + result
        carry =  (a_i + b_i + carry) // 2
        # FIX ME: Update result += ....
        # FIX ME: Update carry =
    if carry == 1:
        result = str(carry) + result #"FIX ME: Update 'result' to the correct value."
    return result # FIX ME return the appropriate string


""" ---------------- PROBLEM 4 ----------------"""


def binary_mul(a, b):
    pass
    # removing all whitespace from the strings
    a = a.replace(' ', '')
    b = b.replace(' ', '')

    # multiplication algorithm
    partial_products = []
    i = 0  # index of the current bit of string 'a' beginning at 0, right-to-left
    for bit in reversed(a):
        if bit == '1':
            partial_products.append(b + i * '0') #"FIXME: Append the appropriate partial product"
        i += 1

    result = '0'
    while len(partial_products) > 0:
        result = binary_add(result, partial_products[0]) #"FIXME: Input the correct arguments"
        del partial_products[0]
    return result # FIXME: Return the appropriate result
