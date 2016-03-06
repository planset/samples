=====================
msgpack samples
=====================

msgpackはJSONのように簡単にシリアライズ・デシリアライズできて、かつ、高速に動作するライブラリ。

C++とrubyが高速ってかいてたような気がする。

* `msgpack <http://msgpack.org/>`_
* `msgpack/msgpack <https://github.com/msgpack/msgpack>`_



python libraries
====================

::

    pip search msgpack
    msgpack-python            - MessagePack (de)serializer.
    msgpack-pure              - MessagePack (de)serializer written in pure Python.
    wzmsgpackrpc              - MessagePack-RPC implementation using Whizzer
    msgpack-rpc-python        - MessagePack RPC


msgpack-python
====================
::
    import msgpack
    data = {"name": "igarashi", age: 100}
    packeddata = msgpack.packb(data)
    print packeddata

    unpackeddata = msgpack.unpackb(packeddata)
    print unpackeddata

msgpack-rpc-python
====================

Server
-------

::

    import msgpackrpc

    class SumServer:
        def sum(self, x, y):
            return x + y

    server = msgpackrpc.Server(SumServer())
    server.listen(msgpackrpc.Address("localhost", 18800))
    server.start()


Client
-------
::

    import msgpackrpc

    client = msgpackrpc.Client(msgpackrpc.Address("localhost", 18800))
    result = client.call('sum', 1, 2)  # = > 3




