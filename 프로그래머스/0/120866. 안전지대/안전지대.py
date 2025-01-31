def solution(board):
    answer = 0 
    di = [0, 1, 0, -1, 0, 1, 1, -1, -1]
    dj = [0, 0, 1, 0, -1, 1, -1, -1, 1] 
    n = len(board) 
    for i in range(n): 
        for j in range(n): 
            flag = True 
            for k in range(9): 
                ni = i + di[k]
                nj = j + dj[k]
                if ni >= 0 and ni < n and nj >= 0 and nj < n and board[ni][nj] == 1: # 8가지 경우 지뢰가 없다면
                    flag = False
                    break
            if flag == True:
                answer += 1

    return answer


print(solution(
     [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]))
print(solution(
     [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]))
print(solution(
     [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]))

