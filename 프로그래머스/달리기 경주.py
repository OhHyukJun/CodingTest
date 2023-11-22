def solution(players, callings):
    answer = []
    play_dict = {}
    index = 0
    for i in players:
        play_dict[i] = index
        index += 1
    
    for i in callings:
        index = play_dict[i]
        if index !=0:
            players[index], players[index-1] = players[index-1], players[index]
            play_dict[players[index]] = index
            play_dict[i] = index-1
    
    answer = players
    return answer
