# main.py

from mathpkg.addition import add
from mathpkg.subtraction import subtract
from mathpkg.multiplication import multiply
from mathpkg.division import divide
from mathpkg.modulus import modulus
from mathpkg.exponentiation import power
from mathpkg.square_root import square_root

def main():
    try:
        # Demonstrate addition
        print("Addition: 7 + 4 =", add(7, 4))
        
        # Demonstrate subtraction
        print("Subtraction: 7 - 4 =", subtract(7, 4))
        
        # Demonstrate multiplication
        print("Multiplication: 7 * 4 =", multiply(7, 4))
        
        # Demonstrate division
        print("Division: 7 / 4 =", divide(7, 4))
        
        # Demonstrate modulus
        print("Modulus: 7 % 4 =", modulus(7, 4))
        
        # Demonstrate exponentiation
        print("Exponentiation: 7 ** 4 =", power(7, 4))
        
        # Demonstrate square root
        print("Square Root: sqrt(36) =", square_root(36))

    except ZeroDivisionError as e:
        print(e)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

