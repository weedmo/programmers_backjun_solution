def solution(my_string, queries):
    for s, e in queries:
        if s == 0:
            my_string = my_string[e::-1] + my_string[e+1:]
        else:
            my_string = my_string[:s] + my_string[e:s-1:-1] + my_string[e+1:]
    return my_string