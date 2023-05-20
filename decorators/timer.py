import time


def timer(msg):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            runtime = round(end - start, 3)  # Abrevia para duas casas decimais
            print(f"Runtime {msg}: {runtime}s")
            return result
        return wrapper
    return decorator
