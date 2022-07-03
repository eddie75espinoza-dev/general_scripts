#

def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    print(a/b)

divide(70, 7)


##

def dec(x):
    x -= 1
    return x

def inc(x):
    x += 1
    return x       

def operate(func, x):
    result = func(x)
    return result

print(operate(dec, 3))  
print(operate(inc, 6))  

##

def star(func):
    def inner(*args, **kwargs):
        print("*" * 10)
        func(*args, **kwargs)
        print("*" * 10)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 10)
        func(*args, **kwargs)
        print("%" * 10)
    return inner


@star
@percent
def printer(msg,x):
    print(msg.center(x))


#printer("{:^10}".format("Hello"))
#printer("hello".center(10))
printer("Hello",10)

#--------------------
import	time

class getTime:
    def __init__(self, function):
        self.function = function
    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.function(*args,**kwargs)
        global t_time
        t_time=[self.function.__name__, time.time()-start]
        return result

@getTime
def sendData(data):
    print(data)
    

data = {
    'id': 97,
    'nombre': 'data',
    'raza': 'humanoide',
    'ocupacion': 'piloto'
}
sendData(data)

#### other decorator

def my_deco(function):
    def wrapper(*args, **kwargs):
        function(*args, **kwargs)
        print('I am decorating your function!')
    return wrapper

@my_deco
def hello(name):
    print(f'Hello {name}, I am calling to decorator')

hello('Eddie')