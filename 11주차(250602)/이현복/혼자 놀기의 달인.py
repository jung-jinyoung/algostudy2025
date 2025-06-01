def solution(cards):
    answer = 0
    lll = len(cards)
    check =[0] * lll
    group_num = 1
    ans = [0]

    def func(start, now, group, count):
        check[now - 1] = group
        if start == now - 1:
            ans.append(count)
            return
        else:
            func(start, cards[now - 1], group, count + 1)

    for i in range(lll):
        if check[i] == 0:
            if cards[i] == i:
                check[i] = group_num
                group_num += 1
            else:
                check[i] = group_num
                func(i, cards[i], group_num, 1)
                group_num += 1
    ans.sort()
    return ans[-1] * ans[-2]