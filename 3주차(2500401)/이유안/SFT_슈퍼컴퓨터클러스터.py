import sys
import math
'''
arr의 mid 를 가장 낮은 성능으로 정할때 
이전까지의 비용 제곱해서 더하다가 b 보다 커지면 false, right = mid-1 
작게끝나면 최소 비용 갈아치우고 left = right +1 

'''
def cal(arr,mid): # 중간 값
    global n,b
    total = 0
    i = 0
    while i<n and arr[i]<= mid :
        total +=(mid-arr[i])**2
        i+=1
        if total > b:
            return False 
    return True 
input = sys.stdin.readline
n,b = map(int, input().split()) # 컴퓨터 수, 예산 , b 이하로 성능 최대화 
arr = list(map(int,input().split()))
arr = sorted(arr)
res = 0

# print(arr) arr 중 가장 낮은 컴퓨터를 d만큼 업그레이드, d^2만큼 비용 , 업그레이드 한번하거나 하지 않거나 
left, right = arr[0],  arr[-1] + int(math.sqrt(b))  
while left<=right:
    mid = (left+right)//2
    # print(left,mid,right)
    r = cal(arr,mid)
    if r:
        if mid>res:
            # print('yes:',mid)
            res = mid 
        left = mid+1
    else:
        right = mid-1 
print(res)
