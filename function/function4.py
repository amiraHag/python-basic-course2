# ---------------------------------
# -- Function Default Parameters --
# ---------------------------------

def say_hello(name="Unknown", age=0, rate=0.0):
    print(f" Hello {name.strip().capitalize()}, your age is {age} and your rate is {rate}")

say_hello("Amira", 30, 9.1)
say_hello(" sara ", 14, 9.8)
say_hello("Ahmed", 32)
say_hello("Mohamed")
say_hello()
