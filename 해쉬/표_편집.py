def solution(n, k, cmd):
    answer = ['O']*n
    index = k
    stack = []
    table = {i:[i - 1, i + 1] for i in range(n)}
    table[0] = [None, 1]
    table[n-1] = [n-2, None]
    for c in cmd:
        if c == "C":
            answer[index] = "X"
            left,right = table[index]
            stack.append([left,index,right])
            if right == None:
                index = table[index][0]
            else:
                index = table[index][1]
            
            if right == None:
                table[left][1] = None
            elif left == None:
                table[right][0] = None
            else:
                table[left][1] = right
                table[right][0] = left
        elif c == "Z":
            left, now, right = stack.pop()
            answer[now] = "O"
            if left == None:
                table[right][0] = now
            elif right == None:
                table[left][1] = now
            else:
                table[right][0] = now
                table[left][1] = now
        
        else:
            c1,c2 = c.split(" ")
            c2 = int(c2)
            if c1 == "U":
                for i in range(c2):
                    index = table[index][0]
            else:
                for i in range(c2):
                    index = table[index][1]
        
    
        
    return "".join(answer)