# from werkzeug.serving import run_simple
from wsgiref.simple_server import make_server
from pprint import pprint



def application(environ, start_response):
    # pprint(env, indent=4)
    # print(start_response)     # <bound method ServerHandler.start_response of <wsgiref.simple_server.ServerHandler instance at 0x7f9e3f250950>>
    # start_response('200 OK', [('Content-Type', 'text/plain; charset=utf-8')])
    # return ['<h1>Hello World!</h1>']
    '''
    from io import StringIO
    stdout = StringIO()
    print("Hello world!", file=stdout)
    print(file=stdout)
    h = sorted(environ.items())
    for k, v in h:
        print(k, '=', repr(v), file=stdout)
    '''
    start_response("200 OK", [('Content-Type','text/html')])
    # return body must be type bytes and iterable
    return ['haha'.encode('utf-8')]


with make_server('10.0.2.15', 8001, application) as httpd:
    print("Serving HTTP on port 8001...")
    httpd.serve_forever()