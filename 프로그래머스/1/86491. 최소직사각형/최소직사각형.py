def solution(sizes):
    max_result = 0
    min_result = 0
    for size in sizes:
        max_result = max(max_result, max(size[0], size[1]))
        min_result = max(min_result, min(size[0], size[1]))
    return max_result * min_result