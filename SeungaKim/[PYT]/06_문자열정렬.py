# 05_문자열정렬하기(https://school.programmers.co.kr/learn/courses/30/lessons/120850)
import re
# regular expression?
def solution(my_string):
    answer = []
    answer = re.findall(r'[0-9]', my_string)
    # for num in answer:
    #     answer_int = int(num)
    temp = [int(num) for num in answer]

    # return temp.sort() -> GPT 참조: list.sort() 는 정렬만하고 None 반환(아무것도반환안함). 그래서 따로 temp return 해줘야함!
    temp.sort()
    return temp

str = "hi12392"
print(solution(str))
