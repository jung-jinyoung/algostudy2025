# 다이아:0, 철:1, 돌:2
damage = [
    [1, 1, 1],
    [5, 1, 1],
    [25, 5, 1]
]


def solution(picks, minerals):
    lll = len(minerals)
    idx = 0
    comp = []
    if sum(picks) * 5 < lll:
        minerals = minerals[:sum(picks) * 5]

    while idx + 5 <= lll:
        arr = minerals[idx:idx + 5]
        comp.append((arr.count('diamond'), arr.count('iron'), arr.count('stone')))
        idx += 5
    if idx != lll:
        arr = minerals[idx:lll]
        comp.append((arr.count('diamond'), arr.count('iron'), arr.count('stone')))

    comp.sort(reverse=1)
    answer = 0
    jdx = 0
    lll2 = len(comp)
    for pick in range(3):
        if jdx + picks[pick] > lll2:
            P = pick
            break
        for i in range(jdx, jdx + picks[pick]):
            answer += (comp[i][0] * damage[pick][0] + comp[i][1] * damage[pick][1] + comp[i][2] * damage[pick][2])
        jdx += picks[pick]
    else:
        return answer
    for i in range(jdx, lll2):
        answer += (comp[i][0] * damage[P][0] + comp[i][1] * damage[P][1] + comp[i][2] * damage[P][2])
    return answer
