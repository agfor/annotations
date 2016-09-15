def convert(func):
    def wrapper(prefix, suffix):
        prefix_type = func.__annotations__["prefix"] # str
        suffix_type = func.__annotations__["suffix"] # str
        result_type = func.__annotations__["return"] # bool

        prefix = prefix_type(prefix) # "" => ""
        suffix = suffix_type(suffix) # "" => ""

        result = func(prefix, suffix) # None
        result = result_type(result) # False
        return result
    return wrapper
