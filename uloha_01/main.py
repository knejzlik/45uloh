import time

data = ["jablko", "banán", "jablko", "pomeranč"]
set_result = set(data)

seen = set()
ordered_result = []
for item in data:
    if item not in seen:
        seen.add(item)
        ordered_result.append(item)

print("Původní data:", data)
print("Set (poradi se nemusi zachovat):", set_result)
print("List se zachovanim poradi:", ordered_result)
print("Závěr: Set NENÍ vždy vhodnější než list.")
