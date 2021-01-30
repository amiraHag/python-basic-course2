# -----------------------------------
# -- Modules => Create Your Module --
# -----------------------------------

import sys
sys.path.append(r"/media/amira/01D5E524022D6350/study/")
print(sys.path)

import amira
print(dir(amira))
amira.sayHello("Amira")
amira.sayHello("  SaRa  ")

amira.sayHowAreYou("    AmIRa")
amira.sayHowAreYou("  SARA   ")


# Alias
import amira as AH
AH.sayHello("AMIRA")
AH.sayHowAreYou("  SarA  ")

from amira import sayHello
sayHello("AmiraH")

from amira import sayHello as say
say("AmiraHM")
