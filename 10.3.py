from copy import copy
from random import randint

# 10.3.1
def isIterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

# 10.3.2
def build_class_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        class_code = f.read()

    namespace = {}
    exec(class_code, namespace)

    class_obj = next((v for v in namespace.values() if isinstance(v, type)), None)
    return class_obj

# 10.3.3
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Виклик функції: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# 10.3.4
def log_instance_creation(cls):
    class Wrapped(cls):
        def __init__(self, *args, **kwargs):
            print(f"[LOG] Створено екземпляр класу: {cls.__name__}")
            super().__init__(*args, **kwargs)
    return Wrapped


