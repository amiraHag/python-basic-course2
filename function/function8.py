# ------------------------
# -- Function Recursion --
# ------------------------
# ---------------------------------------------------------------------
# -- To Understand Recursion, You Need to First Understand Recursion --
# ---------------------------------------------------------------------

def cleanWord(word):

  if len(word) < 2:

    return word

  return cleanWord(word[1:]) if word[0] == word[1] else word[0] + cleanWord(word[1:])


print(cleanWord("AAAAmmmiiira"))
