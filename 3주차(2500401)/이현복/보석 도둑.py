import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
todo = [list(map(int,input().split())) for _ in range(m)]