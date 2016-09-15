def foo(prefix: str,
        suffix: str
        ) -> str:
    if prefix and suffix:
        return prefix + " and " + suffix
    else:
        return None

result = foo("", "")
print(result)
