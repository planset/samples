from twisted.internet import reactor, protocol

import json

d = [{"name":"hoge", "age":20}]

class MyProtocol(protocol.Protocol):
    made = 0
    closed = 0

    def connectionMade(self):
        self.made = 1
        self.transport.write(json.dumps(d))
        
    def connectionLost(self, reason):
        self.closed = 1

    def dataReceived(self, data):
        print data
        self.transport.loseConnection()

class TCPClient(protocol.ClientFactory):
    def buildProtocol(self, addr):
        self.protocol = MyProtocol()
        return self.protocol

client = TCPClient()
reactor.connectTCP('127.0.0.1', 1234, client)
while not client.protocol or not client.protocol.closed:
    reactor.iterate()

