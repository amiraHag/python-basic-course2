# -------------------------------
# -- Built In Functions => Map --
# -------------------------------
# [1] Map Take A Function + Iterator
# [2] Map Called Map Because It Map The Function On Every Element
# [3] The Function Can Be Pre-Defined Function or Lambda Function
# ---------------------------------------------------------------

# Use Map With Predefined Function
def formatText(text):
    return f"- {text.strip().capitalize()} -"

myList = ["Amira", "sARa", "KAT", "HaNY"]
myListFormated = list(map(formatText, myList))
print(type(myListFormated))

for item in myListFormated:
    print(item)

print("*" * 50)

# Use Map With Lambda Function
for item in list(map(lambda text: f"- {text.strip().capitalize()} -", myList)):
    print(item)
