n = int(input())
s = [int(input()) for _ in range(n)]

def f(i, cnt): # cnt는 계단 개수 세는 것 
    if i >= n: # 모든 원소 탐색 다 한 것 (계단 오를 때 마다 개수 세는 것)
        return 0

    if cnt == 2: # 계단을 두번 올랐다
        return f(i + 1, 0)
    else: # 최대효율을 찾는다 (그냥 오르는가(더하는 것) 뛰어넘는가)
        return max(f(i + 1, cnt + 1) + s[i], f(i + 1, 0))
    # s = 계단, f(i + 1, cnt + 1) + s[i] -> 더하는 것 // f(i + 1, 0) -> 뛰어넘는 것

print(f(0, 0))