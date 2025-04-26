def solution(s):
    lll = len(s)
    if lll==1:
        return lll
    else:
        temp=[]
        for length in range(1,lll//2+1):
            string = ''
            idx = 0
            num = 1
            while idx < lll:
                if s[idx:idx+length]==s[idx+length:idx+length*2]:
                    num+=1
                    idx+=length
                else:
                    if num==1:
                        string+=s[idx:idx+length]
                    else:
                        string+=(str(num)+s[idx:idx+length])
                    num=1
                    idx+=length
            temp.append(len(string))
        temp.sort()
        return temp[0]