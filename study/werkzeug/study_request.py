from werkzeug.wrappers import Request, Response


'''
WSGI has two arguments, environ and start_response.
Use Request class to wrap environ, for easier access to request variables like form data, HTTP headers.\
Response is a WSGI application
'''

# application = Response('Hello World')

'''
def application(environ, start_response):
    request = Request(environ)
    response = Response("Hello %s" % request.args.get('name', 'World!'))
    return response(environ, start_response)
'''
@Request.application
def application(request):
    return Response("Hello %s!" % request.args.get('name', 'World!'))
 