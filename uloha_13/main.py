inner_list = [1, 2]
t = (inner_list, 100)

id_before = id(t)
t[0].append(3)
id_after = id(t)

print("ID tuple před změnou:", id_before)
print("ID tuple po změně:  ", id_after)
print("Je ID stejné?", id_before == id_after)
