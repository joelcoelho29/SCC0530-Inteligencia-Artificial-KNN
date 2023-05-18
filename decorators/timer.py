import time

def timer(msg):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print("\nTempo de execucao", msg, ":", end - start)
            return result
        return wrapper
    return decorator