import sys
import subprocess

NETWORK = "10.1.2."

class IPData(object):
    """ip data class"""
    
    def __init__(self, ipstr):
        """"""
        self.ip = ipstr
        self.result = False
        self.pcname = ""
    def get_result_string(self):
        if self.result:
            return ":-)"
        else:
            return "XXX"

def get_pcname(rawout):
    """"""
    result = rawout
    try:
        result = rawout[0].split("\n")[1].split("        ")[0]
    finally:
        pass
    return result


ips = []

for ip4 in range(1, 255):
    try:
        ip = IPData(NETWORK + str(ip4))
        p = subprocess.call(["ping", "-i1", "-c1", ip.ip], stdout=subprocess.PIPE)
        if p == 0:
            ip.result = True
            #proc = subprocess.Popen(["nmblookup","-A",ip.ip], stdout=subprocess.PIPE)
            #out = proc.communicate()
            #ip.pcname = get_pcname(out)
        ips.append(ip)
    except:
        print "error :" + str(ip4)
    finally:
        pass

with open("ipresult.txt", "w") as f:
    for ip in ips:
        f.write("{0:20}\t{1:3}\t{2:20}\n".format(ip.ip, ip.get_result_string(), ip.pcname))



