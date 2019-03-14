with open('z.txt', encoding="utf8") as f:
    lines = f.read().splitlines()

f2 = open("processed.txt", "w")

for l in lines:
    if len(l) > 3:
        lset = set(l)
        if len(lset) <= 7:
            try:
                f2.write(l + "\n")
            except:
                continue
f2.close()
