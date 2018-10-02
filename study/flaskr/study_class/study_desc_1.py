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
            raise AttributeError('Attr {} cannot be retrieved from {}'.format(self.__name, obj))

    def __set__(self, obj, value):
        raise AttributeError('Attr {} cannot  be set in {} of {}'.format(self.__name, obj, value))

    def __delete__(self, obj):
        raise AttributeError('Attr {} cannot be delete in {}'.format(self.__name, obj))


class NonDataDesc(object):

    def __init__(self, name):
        self.__name = name

    def __get__(self, obj, objclass):
        try:
            print 'Retrieving attr {} from {} ...'.format(self.__name, obj)
            return '{} + {}'.format(objclass.x, obj.y)
        except:
            raise AttributeError('Attr {} cannot be retrieved from {}'.format(self.__name, obj))


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


from collections import deque

def get_attr(obj, attr_name):

    def check_desc(obj):
        has_get = hasattr(obj, '__get__')
        has_set = hasattr(obj, '__set__')
        has_del = hasattr(obj, '__delete__')
        if has_get and not has_set and not has_del:
            '''Non Data Descriptor'''
            return 'nd'
        if has_get or has_set or has_del:
            '''Descriptor'''
            return 'd'
        '''Other type object'''
        return 'o'


    def bfs_search(obj, attr_name, find_type='desc'):
        result = None
        rootclass = obj.__class__
        queue = deque([rootclass])
        while queue:
            objclass = queue.popleft()
            attr = objclass.__dict__.get(attr_name)
            if attr:
                attr_type = check_desc(attr)
                if find_type == 'desc':
                    if attr_type == 'd':
                        result = attr.__get__(obj, rootclass)
                        break
                else:
                    result = attr.__get__(obj, rootclass) if attr_type == 'nd' else attr
                    break
            queue.extend(objclass.__bases__)
        return result


    # 1. If attrname is a special (i.e. Python-provided like __class__) attribute for objectname, return it
    if len(attr_name) > 4 and attr_name[0:2] == '__' and attr_name[-2:] == '__' and attr_name in dir(obj):
        return getattr(obj, attr_name)

    # 2. Check objectname.__class__.__dict__ for attrname. If it exists and is a data-descriptor,
    #    return the descriptor result. Search all bases of objectname.__class__ for the same case.
    result = bfs_search(obj, attr_name)
    if result:
        return result

    # 3. Check objectname.__dict__ for attrname, and return if found. If objectname is a class,
    #    search its bases too. If it is a class and a descriptor exists in it or its bases,
    #    return the descriptor result.
    attr = obj.__dict__.get(attr_name)
    if attr:
        if hasattr(attr, '__get__'):
            return attr.__get__(obj, obj.__class__)
        return attr

    if type(obj) == type:
        # TODO
        pass

    # 4. Check objectname.__class__.__dict__ for attrname. If it exists and is a non-data descriptor,
    #    return the descriptor result. If it exists, and is not a descriptor, just return it.
    #    If it exists and is a data descriptor, we shouldn’t be here because we would have returned at point 2.
    #    Search all bases of objectname.__class__for same case.
    result = bfs_search(obj, attr_name, find_type='non_desc_or_other')
    if result:
        return result

    raise AttributeError('Attr {} not exists!')


# Same output
# print obj.data_attr_parent
# print get_attr(obj, 'data_attr_parent')
# print get_attr(obj, '__class__')

# print obj.data_attr_child
# print get_attr(obj, 'data_attr_child')
# obj.__dict__['data_attr_child'] = DataDesc('hahahaha')
# still desc3, because rule 2, cannot be overwritten
# print obj.data_attr_child
# obj.__dict__['data_attr_haha'] = DataDesc('hahahaha')
# print obj.data_attr_haha

# print obj.non_data_attr_child
# print get_attr(obj, 'non_data_attr_child')
# print obj.__dict__

'''Non Data Descriptor been overwritten'''
# obj.non_data_attr_child = 'xyz'
# print obj.non_data_attr_child
# print obj.__dict__

'''Data Descriptor only can be overwriten at class level'''
obj.__dict__['data_attr_child'] = 'xyz'
obj.__class__.data_attr_child = 'abc'
# print obj.data_attr_child
get_attr(obj, 'data_attr_child')


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