mutable_list = [1, 2, 3]
t = (mutable_list, "skupina A")

print("Původní tuple:", t)
t[0].append(4)
print("Po změně vnitřního listu:", t)
