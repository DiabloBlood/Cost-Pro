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
    'PG': 96,
    'PG2': 98,
    'SG': 100,
    'SG2': 100,
    'SF': 100,
    'SF2': 97,
    'PF': 93,
    'PF2': 97,
    'C': 97,
    'C2': 100
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