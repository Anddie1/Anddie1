def login(function):

    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        with open('textfile.txt', 'a+') as f:
            fname = function.__name__
            print(f'{fname} returned value {value}')
            f.write(f'{fname} returned value {value}\n')
        return value
    return wrapper
@login
def add(x , y):
    return x + y


add(5, 2)