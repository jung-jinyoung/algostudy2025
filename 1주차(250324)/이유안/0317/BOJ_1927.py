'''
x 면 넣기
0이면 가장 작은값 pop

'''
import heapq

n = int(input())
numbers = [ int(input()) for _ in range(n)]
# print(numbers)
heap = []

for number in numbers:
    if number == 0:
        if heap:
            x = heapq.heappop(heap)
            print(x)
            continue
        else:
            print(0)
            continue
    heapq.heappush(heap,number)
