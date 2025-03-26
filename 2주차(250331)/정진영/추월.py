import sys

input = sys.stdin.readline

N = int(input())
in_order = [input().strip() for _ in range(N)]
out_order = [input().strip() for _ in range(N)]

# 입구, 출구 자동차 순서 저장 딕셔너리 생성
in_idxs = {car: idx for idx, car in enumerate(in_order)}
out_cars = [in_idxs[car] for car in out_order]


cnt = 0
# 순서를 저장했기 때문에 out_cars에서 확인해야함.
for i in range(N):
    for j in range(i+1, N):
        if out_cars[i] > out_cars[j]:
            cnt += 1
            break  # 추월한 차량만 카운트하므로, 하나만 체크하면 됨

print(cnt)