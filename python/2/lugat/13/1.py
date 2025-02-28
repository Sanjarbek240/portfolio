a = {"first": "developer", "second": "pythonista", "third": "coder"}

b = list(a.values())[0]
for c in a.values():
    if len(c) > len(b):
        b = c

print("uzuni:", b)