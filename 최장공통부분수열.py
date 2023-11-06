""" 
if i ==0 and j == 0:
    LCS[i][j] = 0
elif string_a[i] == string_b[j]:
    LCS[i][j] = LCS[i-1][j-1] + 1
else:
    LCS[i][j] = 0 """