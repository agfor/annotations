from convert16 import convert

def foo(prefix: str,
        suffix: str
        ) -> bool:
    if prefix and suffix:
        return prefix + " and " + suffix
    else:
        return None

foo = convert(foo)

result = foo("", "")
print(result)
