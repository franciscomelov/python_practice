def sockMerchant(n, ar):
    pairs = []
    new_ar = list(ar)

    for i in range(len(new_ar)-1):
        for j in range(i+1, len(new_ar)):
            if new_ar[i] == new_ar[j]:
                pairs.append(new_ar[i])
                pairs.append(new_ar.pop(j))
                break
    return int(len(pairs) / 2)


print(
    sockMerchant(9,[10,20,20,10,10,30,1,50,10,20,1,2,3,4,5,6])
)

""" 
John works at a clothing store. He has a large pile of socks that he must pair by color for sale. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

For example, there are  socks with colors . There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .

Function Description

Complete the sockMerchant function in the editor below. It must return an integer representing the number of matching pairs of socks that are available.

sockMerchant has the following parameter(s):

n: the number of socks in the pile
ar: the colors of each sock
Input Format

The first line contains an integer , the number of socks represented in .
The second line contains  space-separated integers describing the colors  of the socks in the pile.

Constraints

 where 
Output Format

Return the total number of matching pairs of socks that John can sell.

Sample Input

9
10 20 20 10 10 30 50 10 20
Sample Output

3
Explanation
 """