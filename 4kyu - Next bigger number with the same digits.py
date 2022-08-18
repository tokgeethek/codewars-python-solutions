"""
Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:

12 ==> 21
513 ==> 531
2017 ==> 2071
nextBigger(num: 12)   // returns 21
nextBigger(num: 513)  // returns 531
nextBigger(num: 2017) // returns 2071
If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift):

9 ==> -1
111 ==> -1
531 ==> -1
nextBigger(num: 9)   // returns nil
nextBigger(num: 111) // returns nil
nextBigger(num: 531) // returns nil
"""


# solution timed out because of huge numbers
# import itertools

# def next_bigger(n):
#     text = str(n)
#     textlist = [x for x in text]
#     max = int("".join(sorted(textlist,reverse=True)))
    
#     if n == max:
#         return -1
    
#     perm = sorted(set(itertools.permutations(textlist)))
#     for i in range(len(perm)):
#         if perm[i] == tuple(textlist):
#             return int("".join(perm[i+1]))
    
# brute forcing instead
def next_bigger(n):
    text = str(n)
    textlist = [x for x in text]
    max = int("".join(sorted(textlist,reverse=True)))
    min = int("".join(sorted(textlist)))
    
    if n == max:
        return -1
              
    m = n
    while m <= max:
        m += 1
        if int("".join(sorted(list(str(m))))) == min:
            return m