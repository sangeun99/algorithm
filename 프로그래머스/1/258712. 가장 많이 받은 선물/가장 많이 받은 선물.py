def solution(friends, gifts):
    # 이름을 인덱스로
    f_dict = dict()
    for i in range(len(friends)):
        f_dict[friends[i]] = i
        
    # 선물 기록
    f_history = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    for g in gifts:
        g1, g2 = g.split()
        f_history[f_dict[g1]][f_dict[g2]] += 1
    
    # 선물 지수
    f_rate = [0 for _ in range(len(friends))]
    for i in range(len(friends)):
        f_give = sum(f_history[i])
        f_get = 0
        for j in range(len(f_history)):
            f_get += f_history[j][i]
        f_rate[i] = f_give - f_get
    
    get = [0 for _ in range(len(friends))]
    
    for i in range(len(friends)):
        for j in range(len(friends)):
            if f_history[i][j] > f_history[j][i]:
                get[i] += 1
            elif f_history[i][j] == f_history[j][i] and f_rate[i] > f_rate[j]:
                get[i] += 1
    answer = max(get) 
    return answer