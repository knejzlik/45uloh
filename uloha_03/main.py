data = (10, 20, 30)
print("Původní tuple:", data)

try:
    data[0] = 99
except TypeError as e:
    print("Změna prvku v tuple selhala:", e)
