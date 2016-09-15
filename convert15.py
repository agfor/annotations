def convert(func):
    def wrapper(prefix, suffix):
        prefix_type = func.__annotations__["prefix"] # str
        suffix_type = func.__annotations__["suffix"] # str
        result_type = func.__annotations__["return"] # bool

        prefix = prefix_type(prefix) # 3 => "3"
        suffix = suffix_type(suffix) # 4 => "4"

        result = func(prefix, suffix) # "3 and 4"
        result = result_type(result) # True
        return result
    return wrapper
