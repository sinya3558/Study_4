def solution(mats, park):
    answer = -1
    space=[[0]*len(park[0]) for _ in range(len(park))] 
    maxv=0
    
    #공원의 비어있는 공간으로 만들 수 있는 가장 큰 정사각형 구하기
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j]=="-1":
                if i==0 or j==0:
                    space[i][j]=1
                else:
                    space[i][j]=1+min(space[i-1][j], space[i-1][j-1], space[i][j-1])
                maxv=max(maxv, space[i][j])
                
    #지민이가 가진 돗자리 중 깔 수 있는 가장 큰 돗자리 고르기            
    mats.sort(reverse=True)
    for i in mats:
        if maxv>=i:
            answer=i
            break
    
    return answer