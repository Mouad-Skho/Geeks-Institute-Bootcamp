# Exercise 3 : Writing Our Own Modules

# by importing the whole module
import operators
resultadd = operators.addOperator(2, 3)
print(resultadd)
resultdiv = operators.divideOperator(10, 2)
print(resultdiv)

# by importing specific functions
from operators import addOperator, divideOperator
resultadd = addOperator(2, 3)
print(resultadd)
resultdiv = divideOperator(10, 2)
print(resultdiv)

# by using alias
from operators import addOperator as add
resultadd = add(2, 3)
print(resultadd)
from operators import divideOperator as div
resultdiv = div(10, 2)
print(resultdiv)