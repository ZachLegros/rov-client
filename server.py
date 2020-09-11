from apiserver import ApiServer, ApiRoute

def start_server(tel, port):
    class Server(ApiServer): 
        @ApiRoute("/data")
        def addbar(self):
            return {"data": tel.get_data()}

    print(f"Server started on port {port}")
    Server("127.0.0.1", port).serve_forever()    
    