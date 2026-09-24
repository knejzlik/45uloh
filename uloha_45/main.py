keys = ["id1", "id2", "id3"]
vals = ["Alice", "Bob", "Charlie"]

idx = keys.index("id2")
res_list = vals[idx]

d = {"id1": "Alice", "id2": "Bob", "id3": "Charlie"}
res_dict = d["id2"]

print("Výsledek z listů:", res_list)
print("Výsledek ze slovníku:", res_dict)
