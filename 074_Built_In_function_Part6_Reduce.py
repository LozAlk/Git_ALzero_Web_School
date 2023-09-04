# ---------------------------------
# -- Built In Function => Reduce --
# ---------------------------------
# [1] Reduce Take A Function + Iterator
# [2] Reduct Run A Function On First And Second Element And Give Result
# [3] Then Run Function On Result And Third Element
# [4] Then Run Function On Result And Fuorth Element And So On
# [5] Till One Element is Left and This is The Result of The Reduce
# [6] The Function Can Be Pre-Defined Function or Lambda Function 
# ----------------------------------------------------------------------





from functools import reduce


def sumAll (num1, num2):

    return num1 + num2

numbers = [1,8,9,2,100]

#result =reduce(sumAll, numbers)
result =reduce(lambda num1,num2: num1 + num2, numbers)
print(result)

# ((((1+8) +9) +2) +100)