# ---------------------------------------
# -- Function Parameters And Arguments --
# ---------------------------------------

a, b, c = "One", "Two", "Three"

print(f"Number {a}")
print(f"Number {b}")
print(f"Number {c}")

print("*"*40)

# def                     => Function Keyword [Define]
# say_hello()             => Function Name
# name                    => Parameter
# print(f"Hello {name}")  => Task
# say_hello("Ahmed")      => Function Call , Ahmed is The Argument

def say_hello(name):

  print(f"Hello {name}")

say_hello("Amira")
say_hello(a)
say_hello(b)
say_hello(c)
print("*"*40)

def addition(number1, number2):
    return number1 + number2

print(addition(5, 9))

def additionIntegers(number1, number2):
    if type(number1) != int or type(number2) != int:
        return "only integers allowed"
    else:
        return number1 + number2

print(additionIntegers(7, 10))
print(additionIntegers(7, 10.00))
print("*"*40)

def display_full_name(first, middle, last):
    print(f"{first.strip().capitalize()} {middle.strip().upper():.01s} {last.strip().capitalize()}")
display_full_name("amira  ", " hag", "  mustafa")
