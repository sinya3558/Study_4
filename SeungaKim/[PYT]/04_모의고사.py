# 04_모의고사.py (https://school.programmers.co.kr/learn/courses/30/lessons/42840)

def solution(answers):
    most = []
    pattern_1 = [1, 2, 3, 4, 5]
    pattern_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    # 누가 가장 많이 맞췄나?
    cnt_list = []
    cnt_1, cnt_2, cnt_3 = 0, 0, 0

    for idx in range(len(answers)):
        if pattern_1[idx % len(pattern_1)] == answers[idx]: # 반복패턴이라 idx of answer % len(pattern) 으로 나누면 비교 가능
            cnt_1 += 1
        # 잉, gpt 참조: if-elif 쓰면 안되고, if-if-if -> 아하 동시에 체크필요함
        if pattern_2[idx % len(pattern_2)] == answers[idx]:
            cnt_2 += 1
        if pattern_3[idx % len(pattern_3)] == answers[idx]:
            cnt_3 += 1
    
    cnt_list = [cnt_1, cnt_2, cnt_3]
    max_cnt = max(cnt_list)
    # 맞춘 사람 리턴
    for person, cnt in enumerate(cnt_list, start=1):
        if cnt == max_cnt:
            most.append(person)

    return most

ans = [1,3,2,4,2]	
print(solution(ans))