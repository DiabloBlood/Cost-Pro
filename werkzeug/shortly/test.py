from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple
import shortly



@Request.application
def application(request):
    return Response('Hello World!')


import os
print os.path.join(os.path.dirname(__file__), 'static')

# if __name__ == '__main__':
    # run_simple('10.0.2.15', 8001, application)