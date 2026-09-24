user_data = {"name": "Jan", "age": 18}

try:
    print(user_data[0])
except KeyError as e:
    print("Klíč 0 ve slovníku neexistuje (KeyError):", e)
