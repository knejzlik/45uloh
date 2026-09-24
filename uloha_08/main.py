unique_list = [1, 2, 3, 4, 5]
unique_set = {1, 2, 3, 4, 5}

print("První prvek v listu přes index 0:", unique_list[0])

try:
    print(unique_set[0])
except TypeError as e:
    print("Set nepodporuje indexování:", e)
