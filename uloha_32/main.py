data = [10, 20, 30, 40]

original_len = len(data)
dedup_len = len(set(data))

print(f"Původní délka: {original_len}, po deduplikaci: {dedup_len}")
if original_len == dedup_len:
    print("Všechny prvky byly unikátní.")
