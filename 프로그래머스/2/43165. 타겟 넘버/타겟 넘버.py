from itertools import product

def solution(numbers, target):
    answer = 0
    for i in list(product([-1, 1], repeat=len(numbers))):
        s = 0
        for j in range(len(numbers)):
            s += i[j] * numbers[j]
        if s == target:
            answer += 1
    return answer