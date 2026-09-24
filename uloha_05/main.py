lst = [10, 20, 30, 40]
d = {0: 10, 1: 20, 2: 30, 3: 40}

print("List slicing lst[1:3]:", lst[1:3])
try:
    print(d[1:3])
except (TypeError, KeyError) as e:
    print("Slovník nepodporuje slicing:", type(e).__name__)
