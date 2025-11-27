# https://school.programmers.co.kr/learn/courses/30/lessons/42579

# from collections import defaultdict

# def solution(genres, plays):
#     genre_play = defaultdict(list)
#     play_index = defaultdict(list)
    
#     for i in range( len(genres) ):
#         genre = genres[i]
#         play = plays[i]
#         genre_play[genre].append(play)
#         play_index[play].append(i)
        
#     # play가 큰 순서대로 정렬
#     for genre in genres:
#         genre_play[genre].sort(reverse=True)

#     # genre 별 play의 합이 높은 순서대로 정렬한 리스트 생성
#     genre_rank = sorted(genre_play.keys(), key=lambda x:sum(genre_play[x]), reverse=True)
#     best_album = []

#     for genre in genre_rank:
#         temp = []
#         for i in range(min(2, len(genre_play[genre]))):  # 장르별 2개 선택
#             index = play_index[genre_play[genre][i]][:2]    # 번호 낮은 노래 순서대로 2개
#             temp.extend(index)
#         best_album.extend(temp[:2]) # 재생 횟수가 같은 노래로 인해 초과되는 것 방지
            
    
#     return best_album

from collections import defaultdict

def solution(genres, plays):
    genre_plays = defaultdict(list)
    play_idx = defaultdict(list)
    
    for i in range(len(genres)):
        genre_plays[genres[i]].append(plays[i]) # 장르가 key, 플레이가 val
        play_idx[plays[i]].append(i)            # 플레이가 key, 고유번호가 val
    
    for g in genres:
        genre_plays[g].sort(reverse=True)
    
    best_genre = sorted(genre_plays.keys(), key = lambda x:sum(genre_plays[x]), reverse=True)
    best_album = []
    
    for g in best_genre:
        for i in range(min(2, len(genre_plays[g]))):
            album = play_idx[genre_plays[g][i]]
            for j in range(len(album)):
                a = album[j]
                if a not in best_album:
                    best_album.append(a)
                    break
    
    return best_album
