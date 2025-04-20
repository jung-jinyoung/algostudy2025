from collections import defaultdict
def solution(genres, plays):
    answer = []
    playlist1=defaultdict(int)
    playlist2=defaultdict(list)
    lll = len(plays)
    for i in range(lll):
        playlist1[genres[i]]+=plays[i]
        playlist2[genres[i]].append([-plays[i],i])
    lists1 = list(playlist1.items())
    lists1.sort(key = lambda x:-x[1])
    ans=[]
    for G,N in lists1:
        playlist2[G].sort()
        ans.append(playlist2[G][0][1])
        if 1<len(playlist2[G]):
            ans.append(playlist2[G][1][1])

    return ans