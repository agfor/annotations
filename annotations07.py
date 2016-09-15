from pprint import pprint

def foo(prefix: "The first word",
        suffix: "The last word"
        ) -> "The two words with 'and' between them":
    return prefix + " and " + suffix

pprint(foo.__annotations__)
#result = foo("foo", "bar")
#print(result)
