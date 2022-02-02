from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        func(*args, **kwargs)
        end = datetime.now()
        time_elapsed = end - start
        print(f"Execution time: {time_elapsed.total_seconds()} seconds")
    return wrapper

@execution_time
def random_func():
    for _ in range(1, 1000000): 
        pass

@execution_time
def suma(a: int, b: int) -> int:
    return a + b

# random_func()
