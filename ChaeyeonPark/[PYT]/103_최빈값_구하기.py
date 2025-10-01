def solution(array):
    answer = -1
    count=[0]*(max(array)+1)
    maxs=0
    
    for i in array:
        count[i]+=1
    
    for c in count:
        if c== max(count):
            maxs+=1
            if maxs>1:
                return -1
            
    answer=count.index(max(count))
    return answer