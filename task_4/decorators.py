from functools import wraps

def input_error(func):
    """Декоратор для обробки помилок введення користувача"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please"
        except KeyError:
            return "Enter user name"
        except IndexError:
            return "Enter the argument for the command"

    return wrapper

def attrs_count(expected: int, err_msg: str):
    """Декоратор для перевірки кількості аргументів команди"""

    def decorator(func):
        @wraps(func)
        def wrapper(args, *rest, **kwargs):
            if len(args) != expected:
                return f"This command requires exactly {expected} argument(s). {err_msg}"
            return func(args, *rest, **kwargs)
        return wrapper
    return decorator
