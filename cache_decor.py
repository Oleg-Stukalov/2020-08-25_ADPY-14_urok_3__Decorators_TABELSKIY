import time
from collections import OrderedDict


def cachable(param):
    CACHE = OrderedDict()

    def _cachable(old_function):

        def new_function(*args, **kwargs):
            print(len(CACHE))
            key = (old_function.__name__, str(args), str(kwargs))
            result = CACHE.get(key)
            if result is not None:
                return result
            else:
                result = old_function(*args, **kwargs)
                CACHE[key] = result
                if len(CACHE) > param:
                    CACHE.popitem(last=False)
                return result

        return new_function

    return _cachable


@cachable(4)
def concat(str_1, str_2):
    time.sleep(2)
    return f'{str_1}{str_2}'


print(concat('abc', 'erd'), '\n')
print(concat('abc', 'erd1'), '\n')
print(concat('abc', 'erd2'), '\n')
print(concat('abc', 'erd3'), '\n')
print(concat('abc', 'erd4'), '\n')
print(concat('abc', 'erd5'), '\n')
