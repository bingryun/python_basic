def solution(L, x):
    answer = []
    chk_index=0
    for i in range(len(L)) :
        if L[i] > x :
            chk_index=i
            break
        else :
            chk_index=i+1
    L.insert(chk_index,x)
    answer=L
    return answer