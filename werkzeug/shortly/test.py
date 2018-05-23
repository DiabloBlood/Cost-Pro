from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple
import shortly

from pprint import pprint



# @Request.application
def application(environ, start_response):
    request = Request(environ)
    print start_response
    print request.form
    print type(request.form)
    print request.args
    response = Response('hahahah')
    return response(environ, start_response)


row = {
    'PG': 99,
    'PG2': 93,
    'SG': 96,
    'SG2': 99,
    'SF': 99,
    'SF2': 98,
    'PF': 97,
    'PF2': 98,
    'C': 97,
    'C2': 98
}

def get_avg():
    s = 0
    for key in row:
        level = row[key]
        s += level
    return (s + 0.0)/10

# import os
# print os.path.join(os.path.dirname(__file__), 'static')

if __name__ == '__main__':
    # run_simple('10.0.2.15', 8001, application)
    print get_avg()