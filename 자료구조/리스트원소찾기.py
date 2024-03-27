def solution(L, x):
    answer = []
    chk_index=0
    try:
        while True:
            result_index=L.index(x,chk_index)
            answer.append(result_index)
            chk_index=result_index+1
    except ValueError:
            if not answer:
                return [-1]
    return answer