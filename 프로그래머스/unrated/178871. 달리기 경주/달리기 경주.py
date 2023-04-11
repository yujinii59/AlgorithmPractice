def solution(players, callings):
    ranks = dict()
    player_rank = dict()
    for i, player in enumerate(players):
        ranks[i+1] = player
        player_rank[player] = i+1
        
    for calling in callings:
        rnk = player_rank[calling]
        prev = ranks[rnk-1]
        ranks[rnk-1] = calling
        ranks[rnk] = prev
        player_rank[calling] -= 1
        player_rank[prev] += 1
        
    answer = []
    for i in range(len(players)):
        answer.append(ranks[i+1])
    return answer