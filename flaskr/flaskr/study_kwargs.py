from pprint import pprint


def foo(a, b, c, *args, **kwargs):
    pprint(args)
    print type(args)
    print type(kwargs)

foo(1, 2, 3)