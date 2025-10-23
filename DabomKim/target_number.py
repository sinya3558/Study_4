

# 

def dfs(numbers, target, idx, values):
    global cnt              # 전역변수 선언

    if idx == len(numbers):
        if values == target:
            cnt += 1
        return

    dfs(numbers, target, idx + 1, values + numbers[idx])
    dfs(numbers, target, idx + 1, values - numbers[idx])


# cnt 초기화, dfs 호출
def solution(numbers, target):
    global cnt
    cnt = 0   # 전체 경우의 수 초기화

    dfs(numbers, target, 0, 0)

    return cnt

numbers = [4, 1, 2, 1]
target = 4

idx, values,    cnt
0,      0       0
1,      4       0
2,      5
3,      7
4,      8
5,              1