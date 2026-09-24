original_list = [3, 1, 2, 1, 3]
converted_set = set(original_list)
restored_list = list(converted_set)

print("Původní list:", original_list)
print("Restaurovaný list z setu:", restored_list)
print("Rovnají se?", original_list == restored_list)
