def singleton(func):
    _instances = {}

    # *args and **kwargs to denote thw function's arguments
    def get_instance(*args, **kwargs):
        if func not in _instances:
            _instances[func] = func(*args, **kwargs)
        return _instances[func]

    return get_instance


@singleton
class Database:
    def __init__(self):
        print('Loading database')


if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1 == d2)
