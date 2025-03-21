'''
n,m (x,y), k // 가로 세로, 주사위좌표, 명령개수
n * m 지도
이동명령
1 동
2 서
3 북
4 남
'''


r,c,x,y,n = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
orders = list(map(int,input().split()))

dice = [1, 3, 4, 2, 5, 6]
# dice[top][dir] = Bottom
now_num = dict()
for i in range(1,7):
    now_num[i] = 0
# 시작면은 전부 0
dx,dy = [0,0,0,-1,1],[0,1,-1,0,0] # 1,2,3,4
top = 1 # 시작면
for order in orders:
    nx,ny = x+dx[order], y+dy[order]

    if nx<0 or nx>=r or ny<0 or ny>=c:
        continue

    if order == 1:  # 동쪽
        dice[0], dice[1], dice[5], dice[2] = dice[2], dice[0], dice[1], dice[5]
    elif order == 2:  # 서쪽
        dice[0], dice[1], dice[5], dice[2] = dice[1], dice[5], dice[2], dice[0]
    elif order == 3:  # 북쪽
        dice[0], dice[3], dice[5], dice[4] = dice[3], dice[5], dice[4], dice[0]
    elif order == 4:  # 남쪽
        dice[0], dice[3], dice[5], dice[4] = dice[4], dice[0], dice[3], dice[5]

        # 주사위의 상단 값
    top = dice[0]
    bottom = dice[5]

    if arr[nx][ny] == 0:
        arr[nx][ny] = now_num[bottom] # 복사
    else:
        now_num[bottom] = arr[nx][ny]
        arr[nx][ny] = 0

    print(now_num[top])
    x,y, = nx,ny
