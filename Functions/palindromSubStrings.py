

def palindromSubStr(s):
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            k = s[i:j+1]
            if k == k[::-1]:
                print(k)
                
                
palindromSubStr('mamata')