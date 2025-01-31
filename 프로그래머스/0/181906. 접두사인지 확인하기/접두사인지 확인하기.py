def solution(my_string, is_prefix):
    return int(bool(''.join(list(my_string)[:len(is_prefix)]) == is_prefix))