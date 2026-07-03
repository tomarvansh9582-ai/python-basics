
n = int(input())
arr = map(int, input().split())
SL = sorted(set(arr))[-2]
print(SL)