# https://www.acmicpc.net/problem/2983
from bisect import bisect_left

def frogPrincess(D, P):
    # 모든 점에 대해 기울기가 45인 같은 직선 위에 있는 점들의 리스틑 값으로 갖는 해쉬맵 / A, D 방향
    minus_map = {}
    # 모든 점에 대해 기울기가 -45인 같은 직선 위에 있는 점들의 리스틑 값으로 갖는 해쉬맵 / B, C 방향
    plus_map = {}
    for point in P:
        x, y = point
        plus_key = x + y
        minus_key = x - y
        if not plus_key in plus_map:
            plus_map[plus_key] = []
        if not minus_key in minus_map:
            minus_map[minus_key] = []
        plus_map[plus_key].append(point)
        minus_map[minus_key].append(point)
    # D -> A 로 정렬
    for v in minus_map.values(): v.sort()
    # C -> B 로 정렬
    for v in plus_map.values(): v.sort()
    # 현재 위치
    current_point = P[0]
    for direction in D:
        x, y = current_point
        plus_key = x + y
        minus_key = x - y
        plus_index = bisect_left(plus_map[plus_key], current_point)
        minus_index = bisect_left(minus_map[minus_key], current_point)
        # 이동 할 방향의 이동 가능 한 식물들
        available_points = minus_map[minus_key] if direction == 'A' or direction == 'D' else plus_map[plus_key]
        # 다음 이동할 식물의 좌표
        next_index = -1
        if direction == 'A':
            next_index = minus_index + 1
        elif direction == 'B':
            next_index = plus_index + 1
        elif direction == 'C':
            next_index = plus_index - 1
        elif direction == 'D':
            next_index = minus_index - 1

        # 이동 가능한 다른 식물이 없을때 패스
        if next_index < 0 or next_index >= len(available_points):
            continue
        # 이동
        current_point = available_points[next_index]
        # 이동 후 기존 식물 삭제
        del minus_map[minus_key][minus_index]
        del plus_map[plus_key][plus_index]
    return current_point

N, K = map(int, input().split())
D = input()
P = []
for i in range(N):
    P.append(tuple(map(int, input().split())))

print('{} {}'.format(*frogPrincess(D, P)))


