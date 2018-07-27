# -*- coding: utf-8 -*-


# 1. A descriptor is an object that has at least one of the magic methods of
#    __get__, __set__ or __delete__.

# 2. Non-Data Descriptors only have __get__ defined.
# 3. All others are Data Descriptors.

# Notes:
# (1). If you don't define the __get__ method for a descriptor,
#      the descriptor object itself will get returned.

class DataDesc(object):

    def __init__(self, name):
        self.__name = name

    def __get__(self, obj, objclass):
        try:
            print 'Retrieving attr {} from {} ...'.format(self.__name, str(obj))
            return '{} + {}'.format(objclass.x, obj.y)
        except:
            raise AttributeError('Attr {} cannot be retrieved from {}'.format(self.__name, str(obj)))

    def __set__(self, obj):
        raise AttributeError('Attr {} cannot  be set in {}'.format(self.__name, str(obj)))

    def __delete__(self, obj):
        raise AttributeError('Attr {} cannot be delete in {}'.format(self.__name, str(obj)))


class NonDataDesc(object):

    def __init__(self, name):
        self.__name = name

    def __get__(self, obj, objclass):
        try:
            print 'Retrieving attr {} from {} ...'.format(self.__name, str(obj))
            return '{} + {}'.format(objclass.x, obj.y)
        except:
            raise AttributeError('Attr {} cannot be retrieved from {}'.format(self.__name, str(obj)))


class ParentClass(object):
    x = 'x1'
    y = 'y1'
    data_attr_parent = DataDesc('desc1')
    data_attr_child = DataDesc('desc2')

class ChildClass(ParentClass):
    x = 'x2'
    y = 'y2'
    data_attr_child = DataDesc('desc3')
    non_data_attr_child = NonDataDesc('desc4')

obj = ChildClass()

def get_attr(obj, attr_name):

    # 1. If attrname is a special (i.e. Python-provided like __class__) attribute for objectname, return it
    if attr_name in dir(obj):
        return getattr(obj, attr_name)

    if obj.__dict__.get(attr_name):
        attr = obj.__dict__.get(attr_name)
        if hasattr(attr, '__get__'):
            return attr.__get__(obj, obj.__class__)
        return attr

    if obj.__class__.__dict__.get(attr_name):
        attr = obj.__class__.__dict__.get(attr_name)
        if hasattr(attr, '__get__'):
            return attr.__get__(obj, obj.__class__)
        return attr

    # 应该使用BFS检索父类, 这里只检索了第一层
    for super_class in obj.__class__.__bases__:
        if super_class.__dict__.get(attr_name):
            attr = super_class.__dict__.get(attr_name)
            if hasattr(attr, '__get__'):
                return attr.__get__(obj, obj.__class__)
            return attr

    raise AttributeError('Attr {} not exists!')


# Same output
# print obj.data_attr_parent
# print get_attr(obj, 'data_attr_parent')
# print get_attr(obj, '__class__')

class Foo(object):
    x = 4

foo = Foo()
print foo.__dict__
foo.__dict__['x'] = 5
print foo.__dict__
print foo.x




# 1. If attrname is a special (i.e. Python-provided like __class__) attribute for objectname, return it.

# 2. Check objectname.__class__.__dict__ for attrname. If it exists and is a data-descriptor,
#    return the descriptor result. Search all bases of objectname.__class__ for the same case.

# 3. Check objectname.__dict__ for attrname, and return if found. If objectname is a class,
#    search its bases too. If it is a class and a descriptor exists in it or its bases, return the descriptor result.

# 4. Check objectname.__class__.__dict__ for attrname. If it exists and is a non-data descriptor,
#    return the descriptor result. If it exists, and is not a descriptor, just return it.
#    If it exists and is a data descriptor, we shouldn’t be here because we would have returned at point 2.
#    Search all bases of objectname.__class__for same case.

# 5. Raise AttributeError