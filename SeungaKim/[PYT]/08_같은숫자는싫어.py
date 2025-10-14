# 08_같은숫자는싫어.py

def solution(arr):
    answer = []
    # 연속적으로 중복되는 숫자 제거
    duplicated = []
    # 일단, stack 생성
    stack = []
    # stack.push(arr[0])
    for i in range(len(arr)):
        stack.append(arr[i])
    # 스택에서 꺼내면서 역순으로 중복되는 수가 있나 확인 -> 있으면 duplicated 로 넣고 반환
    prev_num = None
    while stack:
        num = stack.pop()
        if num != prev_num:
            # 둘이ㅣ 다르면, answer로
            answer.append(num)
        prev_num = num

    answer.reverse()    # 역순 처리
    return answer

arr = [4,4,4,3,3]
print(solution(arr))
# expected: [4,3]