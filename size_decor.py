from pympler import asizeof


def size_decor(old_function):
    calls = 0
    total_size = 0

    def new_function(*args, **kwargs):
        nonlocal calls, total_size
        calls += 1

        result = old_function(*args, **kwargs)
        size_result = asizeof.asizeof(result)
        total_size += size_result
        medium_size = total_size // calls

        print(f'Вызов:{old_function.__name__}\n'
              f'Размер: {size_result}\n'
              f'В среднем: {medium_size}')
        return result

    return new_function


def parametrized_size_decor(min_size):
    calls = 0
    total_size = 0

    def size_decor(old_function):
        def new_function(*args, **kwargs):
            nonlocal calls, total_size
            calls += 1

            result = old_function(*args, **kwargs)
            size_result = asizeof.asizeof(result)
            total_size += size_result
            medium_size = total_size // calls

            if size_result >= min_size:
                print(f'Вызов:{old_function.__name__}\n'
                      f'Размер: {size_result}\n'
                      f'В среднем: {medium_size}')

            return result

        return new_function

    return size_decor


@size_decor
def foo():
    return [i for i in range(10000)]


@parametrized_size_decor(50000)
def foo2(n):
    return [i for i in range(n)]


if __name__ == '__main__':
    print('***foo()')
    foo()
    print()

    print('***foo2(10)')
    foo2(10)
    print()

    print('***foo2(100000)')
    foo2(100000)
    print()
