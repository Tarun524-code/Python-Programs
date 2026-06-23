class ComplexNumber:
    def __init__(self, real, imag=0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        if not isinstance(other, ComplexNumber):
            return NotImplemented
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        if not isinstance(other, ComplexNumber):
            return NotImplemented
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        if not isinstance(other, ComplexNumber):
            return NotImplemented
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_part, imag_part)

    def __repr__(self):
        return f"ComplexNumber({self.real}, {self.imag})"

    def __str__(self):
        sign = "+" if self.imag >= 0 else "-"
        return f"{self.real} {sign} {abs(self.imag)}i"


if __name__ == "__main__":
    print("Enter first complex number:")
    r1 = float(input("  Real part: "))
    i1 = float(input("  Imaginary part: "))
    c1 = ComplexNumber(r1, i1)

    print("\nEnter second complex number:")
    r2 = float(input("  Real part: "))
    i2 = float(input("  Imaginary part: "))
    c2 = ComplexNumber(r2, i2)

    print("\nStored complex numbers:")
    print(f"  Complex 1: {c1}")
    print(f"  Complex 2: {c2}")

    addition_result = c1 + c2
    subtraction_result = c1 - c2
    multiplication_result = c1 * c2

    print("\nResults:")
    print(addition_result)
    print(subtraction_result)
    print(multiplication_result)
