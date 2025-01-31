import collections

def solution(genres, plays):
    result = []
    play_counts = collections.defaultdict(int)
    genres_inform = collections.defaultdict(list)
    
    for i, (g, p) in enumerate(zip(genres, plays)):
        play_counts[g] += p
        genres_inform[g].append((p, i))
        
    sorted_genres = sorted(genres_inform, 
                           key = lambda x: play_counts[x],
                          reverse = True)
    
    for sg in sorted_genres:
        sorted_inform = sorted(genres_inform[sg],
                              key = lambda x: (-x[0], x[1]))
        result.extend([song[1] for song in sorted_inform[:2]])
        
    return result