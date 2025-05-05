from xmlrpc.server import SimpleXMLRPCServer
from socketserver import ThreadingMixIn
import threading

class ThreadedXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
    pass

class MathService:
    def __init__(self):
        self.lock = threading.Lock()
        self.counters = {
            'add': 0,
            'subtract': 0,
            'min': 0,
            'max': 0
        }

    def magicAdd(self, a, b):
        with self.lock:
            self.counters['add'] += 1
        return a + b

    def magicSubtract(self, a, b):
        with self.lock:
            self.counters['subtract'] += 1
        return a - b

    def magicFindMin(self, a, b, c):
        with self.lock:
            self.counters['min'] += 1
        return min(a, b, c)

    def magicFindMax(self, a, b, c):
        with self.lock:
            self.counters['max'] += 1
        return max(a, b, c)

    def getCounters(self):
        with self.lock:
            return self.counters

server = ThreadedXMLRPCServer(("localhost", 8000), allow_none=True)
server.register_instance(MathService())
print("Server started on port 8000...")
server.serve_forever()
