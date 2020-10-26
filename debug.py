import os
import time
import datetime
import importlib.resources

def decorator(old_function):

    def new_function(*args, **kwargs):
        name_str = old_function.__name__
        ToDayTime = str(datetime.datetime.now())
        old_return = old_function(*args, **kwargs)
        text = os.path.abspath(__file__)

        data = "Time run function: "+ ToDayTime +'\n'+"Name of function: " + name_str + '\n' + "RETURN of function: " + str(old_return) +\
               '\n' + "*args: "+ str(args)  + '\n' + "Path: " + text
        with open('DataTime2', 'w') as f:
            f.write(data)
    return new_function