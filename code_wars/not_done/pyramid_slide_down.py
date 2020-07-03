def longest_slide_down(pyramid):
    biggest = []
    index = 0
    index_in= 0
    index_fi = 1
    for line in pyramid:
        check = 0

        for idx_number in range(len(line[index_in:index_fi])):
            if line[index_in:index_fi][idx_number] > check:
                check = line[index_in:index_fi][idx_number]
                index =idx_number 
                
        print("in",index_in)
        print("fi", index_fi)
        print("array",line[index_in:index_fi])
        biggest.append(check)
        index_in = index
        index_fi = index_in +2
    print(biggest)
    return sum(biggest)


print(longest_slide_down([
              [75],
             [95, 64],
            [17, 47, 82],
          [18, 35, 87, 10],
        [19,  1, 23, 75,  3]])) # 1074
#75, 95, 47, 87, 82, 23, 
"""
https://www.codewars.com/kata/551f23362ff852e2ab000037/train/python
Lyrics...
Pyramids are amazing! Both in architectural and mathematical sense. If you have a computer, you can mess with pyramids even if you are not in Egypt at the time. For example, let's consider the following problem. Imagine that you have a pyramid built of numbers, like this one here:

   /3/
  \7\ 4 
 2 \4\ 6 
8 5 \9\ 3 w
Here comes the task...
Let's say thatthe 'slide down' is the maximum sum of consecutive numbers from the top to the bottom of the pyramid. As you can see, the longest 'slide down' is 3 + 7 + 4 + 9 = 23

Your task is to write a function longestSlideDown (in ruby: longest_slide_down) that takes a pyramid representation as argument and returns its' largest 'slide down'. For example,

longestSlideDown([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]) => 23
By the way...
My tests include some extraordinarily high pyramids so as you can guess, brute-force method is a bad idea unless you have a few centuries to waste. You must come up with something more clever than that.

(c) This task is a lyrical version of the Problem 18 and/or Problem 67 on ProjectEuler.
 """