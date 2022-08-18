"""
Write a function called sumIntervals/sum_intervals() that accepts an array of intervals, and returns the sum of all the interval lengths. Overlapping intervals should only be counted once.

Intervals
Intervals are represented by a pair of integers in the form of an array. The first value of the interval will always be less than the second value. Interval example: [1, 5] is an interval from 1 to 5. The length of this interval is 4.

Overlapping Intervals
List containing overlapping intervals:

[
   [1,4],
   [7, 10],
   [3, 5]
]
The sum of the lengths of these intervals is 7. Since [1, 4] and [3, 5] overlap, we can treat the interval as [1, 5], which has a length of 4.

Examples:
sumIntervals( [
   [1,2],
   [6, 10],
   [11, 15]
] ); // => 9

sumIntervals( [
   [1,4],
   [7, 10],
   [3, 5]
] ); // => 7

sumIntervals( [
   [1,5],
   [10, 20],
   [1, 6],
   [16, 19],
   [5, 11]
] ); // => 19
"""

# def sum_of_intervals(intervals):
#     intervals = sorted(intervals)
#     new = [intervals[0]]
#     for i in range(1,len(intervals)):
#         if intervals[i][0] < new[-1][1]:
#             new.append((new[-1][0],intervals[i][1]))
#             new.pop(-2)
#         else:
#             new.append(intervals[i])
    
#     ans = 0
#     for j in new:
#         ans += j[1] - j[0]
    
#     return ans

def sum_of_intervals(intervals):
    number = []
    maxn = 0
    minn = 0
    for i in intervals:
        if i[1] > maxn:
            maxn = i[1]
        if i[0] < minn:
            minn = i[0]
    for i in range(0, maxn - minn):
        number.append(0)
    for i in intervals:
        for j in range(i[0]-minn, i[1]-minn):
            number[j] = 1   
    return sum(number)