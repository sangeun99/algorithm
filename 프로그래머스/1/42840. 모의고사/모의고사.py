def solution(answers):
    scores = [0, 0, 0]
    for i in range(len(answers)):
        if i % 5 + 1 == answers[i]:
            scores[0] += 1
            
    for i in range(len(answers)):
        if i % 2 == 0:
            if answers[i] == 2:
                scores[1] += 1
        elif i % 8 == 1:
            if answers[i] == 1:
                scores[1] += 1
        elif i % 8 == 3:
            if answers[i] == 3:
                scores[1] += 1                
        elif i % 8 == 5:
            if answers[i] == 4:
                scores[1] += 1                
        elif i % 8 == 7:
            if answers[i] == 5:
                scores[1] += 1
    
    for i in range(len(answers)):
        if i % 10 == 0 or i % 10 == 1:
            if answers[i] == 3:
                scores[2] += 1
        elif i % 10 == 2 or i % 10 == 3:
            if answers[i] == 1:
                scores[2] += 1
        elif i % 10 == 4 or i % 10 == 5:
            if answers[i] == 2:
                scores[2] += 1
        elif i % 10 == 6 or i % 10 == 7:
            if answers[i] == 4:
                scores[2] += 1
        elif i % 10 == 8 or i % 10 == 9:
            if answers[i] == 5:
                scores[2] += 1
    
    answer = []
    for i in range(len(scores)):
        if not answer:
            answer.append(i+1)
        elif scores[answer[0] - 1] == scores[i]:
            answer.append(i+1)
        elif scores[answer[0] - 1] < scores[i]:
            answer = [i+1]
    
    return answer