# https://www.hackerrank.com/challenges/birthday-cake-candles/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
def birthdayCakeCandles(ar):
    ar.sort()
    count = 0
    big = ar[len(ar)-1]
    for i in range(len(ar) -1, -1, -1):
        if big == ar[i]:
            count += 1
        else:
            break
    return count

print(birthdayCakeCandles([4,4,4,1]))

""" 
You are in charge of the cake for your niece's birthday and have decided the cake will have one candle for each year of her total age. When she blows out the candles, she’ll only be able to blow out the tallest ones. Your task is to find out how many candles she can successfully blow out.
"""

