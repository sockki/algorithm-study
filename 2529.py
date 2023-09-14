import sys

k = int(sys.stdin.readline())
bu = list(sys.stdin.readline().strip().replace(" ",""))
bu.append(" ")

a = 0
indexM = 9
resultM = []
indexL = 0
resultL = []
for i in range(k + 1):
    if bu[i] == '>' or bu[i] == " ":
        if a == 0:
            resultM.append(indexM)
        else:
            for x in range(a + 1):
                resultM.append(indexM - a + x)
        indexM -= a + 1
        a = 0
    else:
        a += 1

for i in range(k + 1):
    if bu[i] == '<' or bu[i] == " ":
        if a == 0:
            resultL.append(indexL)
        else:
            for x in range(a + 1):
                resultL.append(indexL + a - x)
        indexL += a + 1
        a = 0
    else:
        a += 1



for i in resultM:
    print(i, end="")
print()
for i in resultL:
    print(i, end="")