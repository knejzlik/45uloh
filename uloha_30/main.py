nested_list = [1, 2]
immutable_tuple = (nested_list, "konstanta")

print("Původní tuple:", immutable_tuple)
immutable_tuple[0].append(3)
print("Tuple po modifikaci vnitřního listu:", immutable_tuple)
