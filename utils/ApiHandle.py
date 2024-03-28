from . import Common

class ApiHandle:
    def __init__(self):
        self._command = None
        pass

    def Process(self, request):
        ret = int(self.get_command(request))

        if int(self._command) == Common.CommandCode.CMD_TEST:
            return "CMD_TEST"
        elif self._command == "2":
            return self.post(Common.API_URL, request.body_arguments)
        else:
            return None

    def get_command(self, request):
        self._command = request.get_query_argument("Command")
        return self._command
    
    def get(self, url, params):
        return self.Process(self, params)

    def post(self, url, data):
        return self.api.post(url, data)