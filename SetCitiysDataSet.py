names = set()

with open("cities15000.txt", encoding="utf-8") as f:
    for line in f:
        parts = line.rstrip("\n").split("\t")
        names.add(parts[2].lower())   # ASCII name, e.g. "moscow"

with open("CitysList", "w", encoding="utf-8") as out:
    for name in sorted(names):
        out.write(name + "\n")

print(len(names), "cities saved to CitysList")