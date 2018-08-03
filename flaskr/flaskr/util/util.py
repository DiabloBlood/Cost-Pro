from collections import deque

from util_classes import MRO



def get_mro(objclass, is_print=False, is_dfs=True):
    mro = MRO()
    return mro(objclass, is_print, is_dfs)


def show_descr(obj):
    return [attr for attr in dir(obj) if attr in ('__get__', '__set__', '__delete__')]