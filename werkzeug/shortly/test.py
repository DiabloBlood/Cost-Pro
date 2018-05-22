from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple
import shortly

from pprint import pprint



# @Request.application
def application(environ, start_response):
    pprint(environ)
    request = Request(environ)
    print request.form
    print type(request.form)
    print request.args
    response = Response('hahahah')
    return response(environ, start_response)






# import os
# print os.path.join(os.path.dirname(__file__), 'static')

if __name__ == '__main__':
    run_simple('10.0.2.15', 8001, application)