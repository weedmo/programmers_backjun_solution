import collections

def solution(array):
    if len(array) == 1:  # 배열의 길이가 1인 경우 바로 반환
        return array[0]
    
    arr_dict = collections.Counter(array)  # 배열의 원소 빈도수 계산
    most_common = arr_dict.most_common()   # 빈도수가 높은 순으로 정렬된 리스트 반환

    # 최빈값이 여러 개인 경우 처리
    if len(most_common) > 1 and most_common[0][1] == most_common[1][1]:
        return -1

    return most_common[0][0]  # 최빈값 반환
