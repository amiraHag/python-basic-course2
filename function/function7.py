# --------------------
# -- Function Scope --
# --------------------

# Global Scope
x = 1

def firstFunction():
  global x
  x = 2
  print(f"Print Variable From Function Scope {x}")

def secondFunction():
  x = 10
  print(f"Print Variable From Function Scope {x}")

firstFunction()
print(f"Print Variable From Global Scope {x}")
secondFunction()
print(f"Print Variable From Global Scope After First Function Is Called {x}")
