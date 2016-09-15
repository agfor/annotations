def foo(prefix: 10 + 5,
        suffix: len,
        ) -> [{()}]:
    return prefix + " and " + suffix

print(foo.__annotations__)
#result = foo("foo", "bar")
#print(result)
