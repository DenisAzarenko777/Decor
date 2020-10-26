import time
import datetime
from debug import decorator

from Decorator.DecoratorWithParams import parametrized_decor


@decorator
def some_function(a, b):
    result = a * b
    return result

some_function(10,8)

@parametrized_decor("DataTime2")
def some_function_for_test(a,b):
    print(a*b)
some_function_for_test(10,90)