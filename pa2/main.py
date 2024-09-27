from pa2 import *

def main():
    print("Testing Primes")
    a = 1
    b = 20
    print(f"A = {a} \nb = {b}")
    print(f"Primes = {primes(a,b)}\n")

    print("Testing bezout_coeffs")
    a = 414
    b = 662
    print(f"A = {a} \nb = {b}")
    print(f"bezout_coeffs = {bezout_coeffs(a,b)}\n")

    print("Testing gcd")
    a = 414
    b = 662
    print(f"A = {a} \nb = {b}")
    print(f"gcd = {gcd(a,b)}\n")

    print("Testing mod_inv")
    a = 3
    b = 11
    print(f"A = {a} \nb = {b}")
    print(f"mod_inv = {mod_inv(a,b)}\n")

    print("Testing solve_mod_equiv")
    a = 3
    b = 4
    m = 7
    low = -5
    high = 5
    print(f"A = {a} \nb = {b} \nLow = {low} \nhigh = {high} \na_inv = {mod_inv(a, m)}")
    print(f"solve_mod_equiv = {solve_mod_equiv(a,b, m, low, high)}\n")

main()