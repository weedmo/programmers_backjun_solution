def solution(my_string):
    str_list = list(my_string) 
    remove_list = ['a', 'e', 'i', 'o', 'u']
    
    result = [char for char in str_list if char not in remove_list]
    
    return ''.join(result)
