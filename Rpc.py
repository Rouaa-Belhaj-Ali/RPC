from  xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client


def sayHello():
    return 'Hello world Form rpcServer'
server = SimpleXMLRPCServer(("localhost", 8000))
print ("Server is listening on port 8000 ...")
server.register_function(sayHello, "sayHello")
server.serve_forever()