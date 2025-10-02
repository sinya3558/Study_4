# 05_최빈값구하기(https://school.programmers.co.kr/learn/courses/30/lessons/120812)
def solution(array): # array = int list
    answer = 0
    max_freq = 0
    for num in set(array):  # 중복 제거
        # print(num)    # identical nums
        # print(array.count(num))

        if array.count(num) > max_freq: #최빈값 초과하면,
            max_freq = array.count(num)
            answer = num    # 최빈값 업데이트
        # 그외, 2개 이상이면,
        elif array.count(num) == max_freq:
            answer = -1

    return answer

arr = [1, 2, 3, 3, 3, 4, 4, 4]
print(solution(arr))