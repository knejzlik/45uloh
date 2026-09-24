shared_object = {"status": "ACTIVE"}
references_list = [shared_object] * 10

print("Index 0 před změnami:", references_list[0]["status"])
references_list[0]["status"] = "INACTIVE"
print("Index 9 po změně na indexu 0:", references_list[9]["status"])
