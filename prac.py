a = ["ABACD"]
b = {}
for i, v in enumerate(a[0]):
    if v in b:
        continue
    b[v] = i

print(b)
