import re
def solution(my_string):
    nums = re.sub('[^0-9]', ' ', my_string)
    nums_list = [int(i) for i in nums.split()]
    return sum(nums_list)