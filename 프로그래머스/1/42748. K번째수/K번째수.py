def solution(array, commands):
    answer = []
    for command in commands:
        target = array[command[0]-1:command[1]]
        target.sort()
        answer.append(target[command[2]-1])
    return answer