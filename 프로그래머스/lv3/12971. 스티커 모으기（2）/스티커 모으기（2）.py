def solution(sticker):
    answer = 0
    length = len(sticker)
    if length == 1:
        return sticker[0]
    elif length == 2:
        return max(sticker)
    else:
        for i in range(2):
            dp = [0,0,0]
            for j in range(length-1):
                dp.append(max(dp[j:j+2]) + sticker[j+i])

            answer = max(answer, dp[-1], dp[-2])

        return answer