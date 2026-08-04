import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print(
            "Time taken to execute by this",
            func.__name__,
            time.time() - start,
            "secs"
        )
    return wrapper

@timer
def message():

    print("message")
    time.sleep(3)


message()
# ==============================================
# Decorator with Function Arguments
# ==============================================
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print(
            "Time taken to execute by this",
            func.__name__,
            time.time() - start,
            "secs"
        )
    return wrapper
@timer
def add(a, b):

    print(a + b)
    time.sleep(3)


add(2, 4)

# ==============================================
# Decorator with **kwargs
# ==============================================
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print(
            "Time taken to execute by this",
            func.__name__,
            time.time() - start,
            "secs"
        )
    return wrapper
@timer
def shopping(**values):

    print(values)


shopping(name="pizza", price=500)