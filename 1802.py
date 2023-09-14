import sys

def search(paper):
    if (len(paper) % 2) == 0:
        print("NO")
        return
    elif len(paper) == 1:
        print("YES")
        return
    else:
        a = int(len(paper) / 2)
        for i in range(1, a + 1):
            if paper[a + i] == paper[a - i]:
                print("NO")
                return
        
        search(paper[a+1:])
        


t = int(sys.stdin.readline())
data = []
data = [sys.stdin.readline().strip() for i in range(t)]

for i in range(t):
    search(data[i])

