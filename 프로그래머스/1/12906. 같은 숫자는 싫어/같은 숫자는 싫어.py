def solution(arr):
    answer = []
    for item in arr:
        if not answer:            
            answer.append(item)
            continue
        if (answer[-1] == item):
            continue
        answer.append(item)
    return answer