
def sample_msgpack_1():
    import msgpack
    data = {"name": "igarashi", "age": 100}
    packeddata = msgpack.packb(data)
    print packeddata

    unpackeddata = msgpack.unpackb(packeddata)
    print unpackeddata

    
if __name__ == "__main__":
    sample_msgpack_1()

