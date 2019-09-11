
age = input("Here comes very classic first input question\nWhat is your age?\n")
print("You will be %d after 10 years" %(int(age) + 10))
print("You will be {} in 20 years, isn't it fascinating".format( int(age)+ 20 ) )

statement = input("Now let me guess the result of the expression you give me: ")        # like 2+2
result = eval(statement)
print("I think the result of {} is equal to {}, isn't it".format(statement,result))