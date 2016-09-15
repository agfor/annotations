from typing import Optional # New in 3.5!

def foo(prefix: str,
        suffix: str
        ) -> Optional[str]:
    if prefix and suffix:
        return prefix + " and " + suffix
    else:
        return None

result = foo("", "")
print(result)
