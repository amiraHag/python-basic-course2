# ------------------------------------------------------
# -- Object Oriented Programming => Getters & Setters --
# ------------------------------------------------------

class Member:

  def __init__(self, name):

    self.__name = name  # Private

  def say_hello(self):

    return f"Hello {self.__name}"

  def get_name(self):  # Getter

    return self.__name

  def set_name(self, new_name):

    self.__name = new_name

one = Member("Amira")

one._Member__name = "MI"
print(one._Member__name)

print(one.get_name())
one.set_name('MHag')
print(one.get_name())
