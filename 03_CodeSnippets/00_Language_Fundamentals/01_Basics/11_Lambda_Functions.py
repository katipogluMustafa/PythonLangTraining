# Lambda Functions

## Lambda functions can have any number of arguments but only one expression.
## The expression is evaluated and returned.
# Lambda functions can be used wherever function objects are required.

square = lambda x: x * x
print(square(7))
print(square(5))

odd_list = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39]

multiples_of_three = list( filter(lambda x: (x % 3 == 0), odd_list) )     # Filter gives the only ones that lambda function evaluates to true
print(multiples_of_three)

double_odd_list = list( map(lambda x: (x * 2), odd_list) )                # lambda applied to each member of odd_list and created new list
print(double_odd_list)
