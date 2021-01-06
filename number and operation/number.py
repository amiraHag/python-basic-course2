#---------------------
#-------Numbers-------
#---------------------

# Integer
print(type(0))
print(type(1))
print(type(100))
print(type(10))
print(type(-10))


# Float
print(type(0.00))
print(type(1.523))
print(type(100.98))
print(type(-100.23))
print(type(-10.12))


# Complex
# Complex= real part + imaginary part (j)
myComplexNumber = 5+6j
print(type(myComplexNumber))
print("My Complex Number is: {}".format(myComplexNumber))
print("The Real Part is: {}".format(myComplexNumber.real))
print("The Imaginary Part is: {}".format(myComplexNumber.imag))

# [1] we can convert from integer to float or complex
# [2] we can convert from float to integer or complex
# [3] we cann't convert complex to any type

print(100)
print(float(100))
print(complex(100))

print(10.99)
print(int(10.99))
print(complex(10.99))

print(5+6j)
# print(int(5+6j)) -> TypeError: can't convert complex to int
# print(float(5+6j)) -> TypeError: can't convert complex to float
