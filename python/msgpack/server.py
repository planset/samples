import msgpackrpc

class SumServer:
    def sum(self, x, y, clientname):
        result = None
        for i in range(1000000):
            result = x + y
        print "{clientname:>10}: {x} + {y} = {result}".format(clientname=clientname, x=x, y=y, result=result)
        return result

server = msgpackrpc.Server(SumServer())
server.listen(msgpackrpc.Address("localhost", 18800))
server.start()


