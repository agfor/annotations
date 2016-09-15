from typing import Union # New in 3.5!

def foo(prefix: str,
        suffix: str
        ) -> Union[str, None]:
    if prefix and suffix:
        return prefix + " and " + suffix
    else:
        return None

result = foo("", "")
print(result)
