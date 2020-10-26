import datetime
import os


def parametrized_decor(parameter):
    def decor(old_function):
        def new_foo(*args, **kwars):
            # здесь код до вызовы функции
            name_str = old_function.__name__
            ToDayTime = str(datetime.datetime.now())
            text = os.path.abspath(__file__)
            result = old_function(*args, **kwars)
            # здесь код после вызовы функции
            data = "Time run function: " + ToDayTime + '\n' + "Name of function: " + name_str + '\n' + "RETURN of function: " + str(
                result) + \
                   '\n' + "*args: " + str(args) + '\n' + "Path: " + text
            with open(parameter, 'a') as f:
                f.write(data)
            return result

        return new_foo

    return decor


@parametrized_decor(parameter=None)
def foo():
    pass