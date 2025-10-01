def solution(answers):
    answer = []
    num=[[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    count=[0,0,0]
    
    for i in range(3):
        for j in range(len(answers)):
            if answers[j]==num[i][j%len(num[i])]:
                count[i]+=1
    
    for c in range(len(count)):
        if count[c]==max(count):
            answer.append(c+1)
    
    answer.sort()    
    
    return answer