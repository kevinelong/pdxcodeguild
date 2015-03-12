tenants = [
    {"name": "Kevin Long",
     "suite": 111},
    {"name": "Kay Long",
     "suite": 112},
    {"name": "John Long",
     "suite": 113},
    {"name": "Jack Richards",
     "suite": 211},
    {"name": "Arthur Wright",
     "suite": 212},
    {"name": "abc",
     "suite": 123},
    {"name": "31 flavors",
     "suite": 231},
    {"name": "!@#$%^&*()",
     "suite": 213}
]
directory = {}
for t in tenants:
    first_letter = t["name"][0]
    if not first_letter in directory:
        directory[first_letter] = []
    directory[first_letter].append(t)
for letter, d in directory.iteritems():
    print("===" + letter + "===")
    for t in d:
        print(" " + t["name"] + " " + str(t["suite"]))