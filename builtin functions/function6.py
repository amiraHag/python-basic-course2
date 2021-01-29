# ----------------------------------
# -- Built In Functions => Reduce --
# ----------------------------------
# [1] Reduce Take A Function + Iterator
# [2] Reduce Run A Function On FIrst and Second Element And Give Result
# [3] Then Run Function On Result And Third Element
# [4] Then Run Function On Rsult And Fourth Element And So On
# [5] Till One ELement is Left And This is The Result of The Reduce
# [6] The Function Can Be Pre-Defined Function or Lambda Function
# ---------------------------------------------------------------

from functools import reduce

def sumNumbers(number1, number2):

  return number1 + number2

numbersList = [10, 9, 3, 2, 90, 100]

result1 = reduce(sumNumbers, numbersList)
print(result1)

result2 = reduce((lambda number1, number2: number1 + number2), numbersList)
print(result2)
