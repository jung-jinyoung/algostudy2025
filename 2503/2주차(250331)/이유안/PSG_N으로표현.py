
def solution(N, number):
    dp = [ set() for _ in range(9) ]
    fis = N
    # dp[0].add(0)
    for P in range(1,9):
        dp[P].add(fis)
        if fis == number:
            return P
        fis= fis*10+N
    
    for i in range(2,9):
        for j in range(1,i):
            for x in dp[i-j]:
                for y in dp[j]:
                    dp[i].add(x+y)
                    if x+y == number:
                        return i 
                    
                    dp[i].add(x*y)
                    if x*y == number:
                        return i 

                    if y!=0:
                        dp[i].add(int(x//y))
                        if x//y == number:
                            return i
                    if x!=0:
                        dp[i].add(int(y//x))
                        if y//x == number:
                            return i                    
                    dp[i].add(x-y)
                    if (x-y) == number:
                        return i 
                    dp[i].add(y-x)
                    if (y-x) == number:
                        return i 
                    
                
            
    return -1