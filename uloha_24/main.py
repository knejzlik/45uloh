s = {10, 20, 30}

try:
    print(s[0])
except TypeError as e:
    print("Set nelze indexovat:", e)
