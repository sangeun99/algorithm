def solution(players, callings):
    answer = []
    p_i_dict = dict()
    i_p_dict = dict()
    for i in range(len(players)):
        p_i_dict[players[i]] = i
        i_p_dict[i] = players[i]
    for c in callings:
        s_index = p_i_dict[c]
        t_index = p_i_dict[c]-1
        t_name = i_p_dict[t_index]
        p_i_dict[c] = t_index
        p_i_dict[t_name] = s_index
        i_p_dict[s_index] = t_name
        i_p_dict[t_index] = c
    for i in range(len(players)):
        answer.append(i_p_dict[i])
    return answer