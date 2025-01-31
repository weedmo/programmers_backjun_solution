import collections
def solution(array, n):
    counter_array = collections.Counter(array)
    return counter_array[n]