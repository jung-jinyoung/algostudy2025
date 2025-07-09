def solution(m, n, startX, startY, balls):
    answer = []
    # m 가로 n 세로 공위치 startX Y 공들 위치 balls
    def f(x, y):
        a = int((startX - x) ** 2 + (startY + y) ** 2)  # x 축
        b = int((startX + x) ** 2 + (startY - y) ** 2)  # y 축
        c = int((startX - x) ** 2 + (startY - (2 * n - y)) ** 2)# x축 위
        d = int((startX - (2 * m - x)) ** 2 + (startY - y) ** 2)# y축 위
        if startX == x:
            if startY > y:
                a = b + 1
            else:
                c = d + 1
        elif startY == y:
            if startX > x:
                b = a + 1
            else:
                d = c + 1
        res = min(a, b, c, d)
        return res
    
    for i in balls:
        asd = f(i[0], i[1])
        answer.append(asd)
    return answer