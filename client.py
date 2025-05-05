import xmlrpc.client
import random

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/", allow_none=True)

for _ in range(1000):
    op = random.choice(["add", "subtract", "min", "max"])
    if op == "add":
        proxy.magicAdd(random.random() * 100, random.random() * 100)
    elif op == "subtract":
        proxy.magicSubtract(random.random() * 100, random.random() * 100)
    elif op == "min":
        proxy.magicFindMin(random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))
    elif op == "max":
        proxy.magicFindMax(random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))

counters = proxy.getCounters()
print("Operation Counters:", counters)
