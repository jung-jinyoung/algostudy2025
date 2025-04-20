from collections import defaultdict
def solution(s):
    check = defaultdict(int)
    ans = []
    s = s[2:-2].split('},{')
    s.sort(key = len)
    first = 1
    for string in s:
        if first:
            first^=1
            ans.append(int(string))
            check[string]=1
        else:
            temp = string.split(',')
            for c in temp:
                if check[c]==0:
                    check[c]^=1
                    ans.append(int(c))
                    break
    return ans