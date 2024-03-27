import .Common

class ApiHandle:
    def __init__(self):
        self._command = None
        pass

    def Process(self, request):
        self.get_command(request)
        



        if int(self._command) == "1":
            return self.get(Common.API_URL, request.query_arguments)
        elif self._command == "2":
            return self.post(Common.API_URL, request.body_arguments)
        else:
            return None

    def get_command(self, request):
        self._command = request.get_query_argument("Command")
        return self._command
    
    def get(self, url, params):
        return self.api.get(url, params)

    def post(self, url, data):
        return self.api.post(url, data)