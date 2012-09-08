from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor

class Echo(Protocol):
      
    def connectionMade(self):
        self.factory.numProtocols = self.factory.numProtocols + 1
        
    def connectionLost(self, reason):
        self.factory.numProtocols = self.factory.numProtocols - 1
    
    def dataReceived(self, data):
        line = "p=%s, receive=%s" % (self.factory.numProtocols, data)
        print line
        with open("log", "a") as f:
            f.write(line)
        self.transport.write(data)

class EchoFactory(Factory):  # Factory for your protocol
    protocol = Echo
    numProtocols = 0


def getEchoFactory():
    factory = EchoFactory()
    factory.protocol = Echo
    factory.numProtocols = 0
    return factory


reactor.listenTCP(1234, getEchoFactory())
reactor.run()

