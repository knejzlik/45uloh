lst = [1, 2, 3]
tpl = (1, 2, 3)

lst[0] = 99
print("Upravený list:", lst)

try:
    tpl[0] = 99
except TypeError as e:
    print("Tuple neumožňuje změnu:", e)
