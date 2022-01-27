from functools import reduce 


nums = [3,2,6,8,4,6,2,9]
'''filter/map/reduce takes two arg 1.func 2.iterable'''
evens = list(filter(lambda n:n%2==0,nums))
print(evens)

doubles = list(map(lambda n:n+2,evens))
print(doubles)

sum = reduce(lambda a,b:a+b,doubles)
print(sum)


'''Map takes all objects in a list and allows you to apply a function to it
   whereas Filter takes all objects in a list and
   runs that through a function to create a new list with all objects that return True in that function. '''

'''reduce() is useful when you need to apply a function to an iterable and reduce it to a single cumulative value. '''