# ----------------------------------
# -- Built In Functions => Filter --
# ----------------------------------
# [1] Filter Take A Function + Iterator
# [2] Filter Run A Function On Every Element
# [3] The Function Can Be Pre-Defined Function or Lambda Function
# [4] Filter Out All Elements For Which The Function Return True
# [5] The Function Need To Return Boolean Value
# ---------------------------------------------------------------

# Example 1

def checkNumberValue(inputNumber):
    return inputNumber > 10

numberList = [1, 3, 6, 9, 10, 20, 50, 5, 100]
numberCheckResult= filter(checkNumberValue, numberList)

for numberItem in numberCheckResult:
    print(numberItem)

print("*" * 40)

# Example 2

def checkName(inputText):
    return inputText.startswith("A")
myTextList = ["Amira", "sARa", "KAT", "HaNY", "Ahmed", "AmORa"]
myTextFormatedResult = filter(checkName, myTextList)

for itemText in myTextFormatedResult:
    print(itemText)

print("*" * 40)

for itemText in filter((lambda inputText: inputText.startswith("A")),myTextList):
    print(itemText)
