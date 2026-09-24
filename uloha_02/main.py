mutable_item = [1, 2, 3]

lst = []
lst.append(mutable_item)
print("Vložení do listu úspěšné:", lst)

try:
    s = set()
    s.add(mutable_item)
except TypeError as e:
    print("Vložení do setu selhalo (TypeError):", e)
