from rest_framework.response import Response

# {
#     message:
#     response:
#     code:
# }


class CustomResponse:

    def __init__(self):
       
        self.http_code = {
            'ok':200,
            'created':201,
            'bad_request':400,
            'unauthorized':401,
            'internal':500
            
            }
     

    def error(self, message):

        body = {
            'error' : message
        }

        return Response(body,status=self.http_code['bad_request'])

    def message(self, message):
        body = {
            'message' : message
        }
        return Response(body,status=self.http_code['ok'])

    def data(self, data):
        body = {
            'data':data
        }
        return Response(body,status=self.http_code['ok'])
    
    def authError(self):
        
        body = {
            'error': 'User unauthorized'
        }
        return Response(body,status=self.http_code['unauthorized'])
    
    def fieldError(self,field):
        body = {
            'message':'The given data was invalid',
            'error' : 'The '+field+' is required'
        }
        return Response(body,status=self.http_code['bad_request'])

