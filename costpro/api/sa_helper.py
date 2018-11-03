import inspect
import datetime

from costpro import db
from costpro import model
from costpro.utils import io



def get_model_columns(table_name):
    columns = None
    for name, obj_class in inspect.getmembers(model, inspect.isclass):
        if name == table_name and issubclass(obj_class, db.Model):
            columns = [{'Header': col.key, 'accessor': col.key} for col in \
                db.inspect(obj_class).mapper.column_attrs]
    return columns


def object_as_dict(obj):
    row = {col.key: getattr(obj, col.key) for col in db.inspect(obj).mapper.column_attrs}
    for key in row:
        value = row[key]
        if isinstance(value, datetime.date):
            value = value.strftime("%m/%d/%Y")
        row[key] = value
    return row


def get_table_obj(table_name):
    for name, obj_class in inspect.getmembers(model, inspect.isclass):
        if issubclass(obj_class, db.Model) and obj_class.__tablename__ == table_name:
            return obj_class
    raise ValueError('Table name not exists!')


class GridHelper(object):

    def __init__(self, b64_params, table):
        self.params = io.b64_to_dict(b64_params)

        if isinstance(table, str):
            self.table = self._get_table_obj(table)
        elif issubclass(table, db.Model):
            self.table = table
        else:
            raise TypeError('Param `table` must either be a string or a subclass of db.Model!')

    def _object_as_dict(self, obj):
        return object_as_dict(obj)

    def _get_table_obj(self, table_name):
        return get_table_obj(table_name)

    def _build_query_result(self):
        params = self.params
        query_obj = db.session.query(self.table)

        if params['sorted']:
            for sort in params['sorted']:
                col_clause = db.column(sort['id'])
                col_clause = col_clause.desc() if sort['desc'] else col_clause.asc()
                query_obj = query_obj.order_by(col_clause)
        else:
            query_obj = query_obj.order_by(self.table.id.asc())

        if params['filtered']:
            for fil in params['filtered']:
                fil_clause = db.column(fil['id']).like('%{}%'.format(fil['value']))
                query_obj = query_obj.filter(fil_clause)

        query_obj = query_obj.paginate(page=params['page'], per_page=params['pageSize']) 

        return query_obj


    def process(self):
        query_result = self._build_query_result()
        total_pages = int(query_result.total / self.params['pageSize'])
        rows = [self._object_as_dict(obj) for obj in query_result.items]
        return rows, total_pages, query_result.total



